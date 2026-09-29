# Importing packages
import os
import requests
import json
from datetime import datetime
import time
import logging
from dotenv import load_dotenv

# Enable logger
logger = logging.getLogger(__name__)

# Creating the function
def extract_json(url:str, data_dir:str, timestamp:str, max_retry:int, delay:int):
    """Extracts JSON from specified URL and saves it locally in the data_dir

    Args:
        url (str): The URL we want to download JSON from
        data_dir (str): Where to save the data
        timestamp (str): The output's filename
        max_retry (int): The number of times to retry calling the API
        delay (int): How long to wait between retries (seconds)
    """

    os.makedirs(data_dir, exist_ok=True)

    # Create the filename for the extracted data
    filename = f"{data_dir}/bike_points_{timestamp}.json"

    # Set up variables for retry settings in case API fails
    attempt = 0

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