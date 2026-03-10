#!/usr/bin/env python3
"""
ISS ETL Pipeline Script (MySQL Version)

Extracts current ISS location from the Open Notify API,
transforms the JSON into tabular format,
and inserts records into a MySQL database.
"""

import sys
import os
import requests
import logging
import mysql.connector
from datetime import datetime


# --------------------------
# Logger Setup
# --------------------------
logger = logging.getLogger("iss_logger")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# --------------------------
# Extract
# --------------------------
def extract():
    url = "http://api.open-notify.org/iss-now.json"

    try:
        logger.info("Extracting ISS data from API...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info("Data successfully extracted.")
        return data

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        sys.exit(1)


# --------------------------
# Transform
# --------------------------
def transform(data):

    try:
        timestamp = datetime.fromtimestamp(data["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")

        record = {
            "message": data["message"],
            "latitude": data["iss_position"]["latitude"],
            "longitude": data["iss_position"]["longitude"],
            "timestamp": timestamp
        }

        return record

    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        sys.exit(1)


# --------------------------
# Register Reporter
# --------------------------
def register_reporter(db, reporter_id, reporter_name):

    cursor = db.cursor()

    try:
        check_query = "SELECT reporter_id FROM reporters WHERE reporter_id = %s"
        cursor.execute(check_query, (reporter_id,))
        result = cursor.fetchone()

        if result is None:
            insert_query = """
            INSERT INTO reporters (reporter_id, reporter_name)
            VALUES (%s, %s)
            """
            cursor.execute(insert_query, (reporter_id, reporter_name))
            db.commit()
            logger.info("Reporter registered.")
        else:
            logger.info("Reporter already exists.")

    except Exception as e:
        logger.error(f"Reporter registration failed: {e}")

    finally:
        cursor.close()


# --------------------------
# Load (Insert into MySQL)
# --------------------------
def load(db, record, reporter_id):

    cursor = db.cursor()

    try:
        insert_query = """
        INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            record["message"],
            record["latitude"],
            record["longitude"],
            record["timestamp"],
            reporter_id
        )

        cursor.execute(insert_query, values)
        db.commit()

        logger.info("ISS location inserted into database.")

    except Exception as e:
        logger.error(f"Database insert failed: {e}")

    finally:
        cursor.close()


# --------------------------
# Main
# --------------------------
def main():

    reporter_id = "ced5jz"
    reporter_name = "Nimisha Vadlamudi"

    try:
        db = mysql.connector.connect(
            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSER"),
            password=os.getenv("DBPASS"),
            database="iss"
        )

        logger.info("Connected to MySQL database.")

        register_reporter(db, reporter_id, reporter_name)

        data = extract()
        record = transform(data)

        load(db, record, reporter_id)

        logger.info("ETL pipeline completed successfully.")

    except mysql.connector.Error as err:
        logger.error(f"MySQL connection failed: {err}")
        sys.exit(1)

    finally:
        if 'db' in locals() and db.is_connected():
            db.close()
            logger.info("Database connection closed.")


if __name__ == "__main__":
    main()
    