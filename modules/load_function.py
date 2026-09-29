import os
import boto3
from dotenv import load_dotenv
import logging
from datetime import datetime

# Set up logger
logger = logging.getLogger()

# Create define the function
def load_files_to_s3(data_dir:str, AWS_ACCESS_KEY:str, AWS_SECRET_ACCESS_KEY:str, AWS_BUCKET_NAME:str):
    """Uploads all files in the directory to s3.

    Args:
        data_dir (str): Where the data is
        AWS_ACCESS_KEY (str): Linked to AWS IAM User
        AWS_SECRET_ACCESS_KEY (str): Linked to AWS IAM User
        AWS_BUCKET_NAME (str): S3 bucket to upload to
    """

    # Setting up s3 client
    s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    # Setting up variables to upload files to s3
    files_to_upload = os.listdir(data_dir)

    for file in files_to_upload:
        file_to_upload = f'{data_dir}/{file}'

        try:
            #Uploading files to s3
            s3_client.upload_file(file_to_upload,AWS_BUCKET_NAME,file)
            print(f'{file} uploaded successfuly.')

            # Logging success
            logger.info(f'File {file} uploaded successfuly.')

            # Removing the file from our local device
            os.remove(file_to_upload)

        # Error handling
        except Exception as e:
            print(f'An error has occured: {e}.')

            # Logging failure
            logger.error(f'An error has occured: {e}.')