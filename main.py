# Retrieving logging function from log_initialise.py and import other packages
from modules.log_initialise import setup_logging
from datetime import datetime

# Create a timestamp for the filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Setting up and testing logger
logger = setup_logging('logs', timestamp)
logger.info('Logger successfully initialised.')