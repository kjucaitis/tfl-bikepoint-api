# Importing packages
import os
import requests
import json
from datetime import datetime
import time
import logging
from dotenv import load_dotenv

# API endpoint where we are extracting the data from
url = 'https://api.tfl.gov.uk/BikePoint/'

# Create a folder to store our extracted data
data_folder = 'data'
os.makedirs(data_folder, exist_ok=True)

# Create a timestamp for the filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Create the filename for the extracted data
filename = f"{data_folder}/bike_points_{timestamp}.json"

# Create a folder for log files
log_dir = 'log'
os.makedirs(log_dir, exist_ok=True)
log_filename = f"{log_dir}/bike_points_{timestamp}.log"

# Configure logging so messages are written to the log file
logging.basicConfig(
    filename = log_filename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

# Create a logger and confirm that it has been successfully set up
logger = logging.getLogger()
logger.info('Logger successfully initialised')

# Set up variables for retry settings in case API fails
max_retry = 5
attempt = 0
delay = 10

# Define our while loop to keep trying until maximum number of attempts is reached
while attempt < max_retry:

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Retrieve the status code
    status_code = response.status_code

    # IF statement based on the status code
    if 200 <= status_code < 300:

        # Convert the response to JSON format
        data = response.json()

        # Check the API returned any data (is not all empty) before trying to save it
        if len(data) > 0:
            try:

                # Open the file in write mode and save the extracted data
                with open(filename, 'w') as file:
                    json.dump(data, file)

                # Print the success comments
                print(f'File {filename} was successfully saved')
                logger.info(f'File {filename} was successfully saved')

            # Handle errors that occur while creating or writing to the file
            except Exception as e:
                print(f'An error has occured: {e}')
                logger.error(f'An error has occured: {e}')
            break

        # If API request succeeded, but not data was returned
        else:
            print('No data returned')

            # Add logger warning
            logger.warning('No data returned')

            break

    # ELIF statement for client or server-side errors
    elif status_code < 200 or status_code >= 500:
        time.sleep(delay)
        attempt += 1
        print(f'Status code: {status_code}. Retrying. Attempt number {attempt}')

        # Add logger info
        logger.info(f'Status code: {status_code}. Retrying. Attempt number {attempt}')

    # ELSE statement for if the error is 300-400, we want to emphasize the need for fixing
    else:
        print(f'Error. Status code {status_code}. Fixing required')

        # Add logger info
        logger.critical(f'Error. Status code {status_code}. Fixing required')

        # Final break to stop the while loop fully
        break