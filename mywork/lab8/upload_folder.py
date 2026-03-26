import boto3
import argparse
import os
import logging

# set up logging
logging.basicConfig(level=logging.INFO)

def parse_args():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description="Upload files to S3")
    parser.add_argument("input_folder", help="Folder with files to upload")
    parser.add_argument("destination", help="S3 bucket/prefix (e.g. ds2002-ced5jz/folder/)")
    return parser.parse_args()

def upload(input_folder, destination):
    """
    Upload all files from input_folder to S3 destination
    """
    try:
        s3 = boto3.client('s3', region_name='us-east-1')

        bucket, prefix = destination.split('/', 1)

        for file in os.listdir(input_folder):
            if file.endswith(".csv"):
                local_path = os.path.join(input_folder, file)
                s3_key = prefix + file

                logging.info(f"Uploading {file}...")
                with open(local_path, 'rb') as f:
                    s3.put_object(
                        Bucket=bucket,
                        Key=s3_key,
                        Body=f
                    )

        logging.info("Upload complete!")

    except Exception as e:
        logging.error(f"Error: {e}")

def main():
    args = parse_args()
    upload(args.input_folder, args.destination)
    logging.info("Script finished")

if __name__ == "__main__":
    main()