#!/usr/bin/env python3
"""
ISS ETL Pipeline Script

Extracts current ISS location from the Open Notify API,
transforms the JSON into tabular format,
and appends the record to a CSV file.
"""

import sys
import os
import requests
import pandas as pd
import logging
from datetime import datetime


# --------------------------
# Logger Setup
# --------------------------
logger = logging.getLogger("iss_logger")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def extract():
    """
    Extract function:
    Calls the ISS location API and returns parsed JSON data.
    Handles errors gracefully.
    """
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


def transform(data):
    """
    Transform function:
    Converts JSON data into a single-row pandas DataFrame.
    Converts UNIX timestamp into readable datetime format.
    """
    logger.info("Transforming JSON data into tabular format...")

    try:
        timestamp = pd.to_datetime(data["timestamp"], unit="s")
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]

        df = pd.DataFrame([{
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "latitude": latitude,
            "longitude": longitude
        }])

        logger.info("Transformation successful.")
        return df

    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        sys.exit(1)


def load(df, filename):
    """
    Load function:
    Appends the transformed DataFrame to a CSV file.
    Creates the file if it does not exist.
    """
    logger.info(f"Loading data into {filename}...")

    try:
        file_exists = os.path.exists(filename)

        if file_exists:
            existing_df = pd.read_csv(filename)
            combined_df = pd.concat([existing_df, df], ignore_index=True)
        else:
            combined_df = df

        combined_df.to_csv(filename, index=False)
        logger.info("Data successfully written to CSV.")

    except Exception as e:
        logger.error(f"Load step failed: {e}")
        sys.exit(1)


def main():
    """
    Main function:
    Orchestrates the ETL workflow.
    """
    if len(sys.argv) != 2:
        logger.error("Usage: python iss.py <output_file.csv>")
        sys.exit(1)

    output_file = sys.argv[1]

    data = extract()
    df = transform(data)
    load(df, output_file)

    logger.info("ETL pipeline completed successfully.")


if __name__ == "__main__":
    main()
