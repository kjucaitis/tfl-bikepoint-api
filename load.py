import os
import boto3
from dotenv import load_dotenv

# Load the .env file to access our variables
load_dotenv()

# Bring through our keys
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# Setting up s3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

# Setting up variables to upload files to s3
files_to_upload = os.listdir('data')

for file in files_to_upload:
    file_to_upload = f'data/{file}'

    try:
        #Uploading files to s3
        s3_client.upload_file(file_to_upload,AWS_BUCKET_NAME,file)
        print(f'{file} uploaded successfuly.')

        # Removing the file from our local device
        os.remove(file_to_upload)

    # Error handling
    except Exception as e:
        print(f'An error has occured: {e}.')