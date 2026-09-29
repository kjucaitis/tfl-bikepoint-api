# Retrieving logging function from log_initialise.py and import other packages
from modules.log_initialise import setup_logging
from modules.extract_function import extract_json
from datetime import datetime

# Create a timestamp for the filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Setting up and testing logger
logger = setup_logging('logs', timestamp)
logger.info('Logger successfully initialised.')

# API endpoint where we are extracting the data from
url = 'https://api.tfl.gov.uk/BikePoint/'

# Create a folder to store our extracted data
data_dir = 'data'

# Set up variables for retry settings in case API fails
max_retry = 5
delay = 10

# Running extract_function.py
extract_json(url,data_dir,timestamp,max_retry,delay)