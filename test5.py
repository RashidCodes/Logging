# Displaying date/time in messages 

import logging 

# logging.basicConfig(format='%(asctime)s %(message)s') 
# logging.warning('is when this event was logged.')


# If you need more control over the formatting of the date/time, provide a datefmt argument to basicConfig, as shown below
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.warning('is when this event was logged.')

