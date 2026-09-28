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
file_to_upload = 'data/bike_points_2026-09-28_10-49-10.json'
filename_s3 = 'bike_points_2026-09-28_10-49-10.json'

# Uploading files to s3
s3_client.upload_file(file_to_upload,AWS_BUCKET_NAME,filename_s3)