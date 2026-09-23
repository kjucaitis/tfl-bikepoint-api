# Importing packages
import os
import requests
import json
from datetime import datetime

# API endpoint where we are extracting the data from
url = 'https://api.tfl.gov.uk/BikePoint/'

# Create a folder to store our extracted data
data_folder = 'data'
os.makedirs(data_folder, exist_ok=True)

# Create a timestamp for the filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Create the filename for the extracted data
filename = f"{data_folder}/bike_points_{timestamp}.json"

# Send a GET request to the API endpoint
response = requests.get(url)

# Convert the response to JSON format
data = response.json()

# Open the file in write mode and save the extracted data
with open(filename, 'w') as file:
    json.dump(data, file)

# Retreieve the status code
status_code = response.status_code

