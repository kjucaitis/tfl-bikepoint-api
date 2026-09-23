# Importing packages
import os
import requests
import json
from datetime import datetime
import time

# API endpoint where we are extracting the data from
url = 'https://api.tfl.gov.uk/BikePoint/'

# Create a folder to store our extracted data
data_folder = 'data'
os.makedirs(data_folder, exist_ok=True)

# Create a timestamp for the filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Create the filename for the extracted data
filename = f"{data_folder}/bike_points_{timestamp}.json"

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

        # Open the file in write mode and save the extracted data
        with open(filename, 'w') as file:
            json.dump(data, file)

        # Print the success comment
        print(f'File {filename} was successfully saved')

        # Add a break clause to stop the while loop if the pull was successful
        break

    # ELIF statement for client or server-side errors
    elif status_code < 200 or status_code >= 500:
        time.sleep(delay)
        attempt += 1
        print(f'Status code: {status_code}. Retrying. Attempt number {attempt}')

    # ELSE statement for if the error is 300-400, we want to emphasize the need for fixing
    else:
        print(f'Error. Status code {status_code}. Fixing required')

        # Final break to stop the while loop fully
        break




