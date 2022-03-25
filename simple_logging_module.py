import logging 
import logging.config


# add a fileconfig if necessary
logging.config.fileConfig('logging.conf')

# create a logger
# getLogger() returns a reference to a logger instance with the specified name if it is provided, or root if it is not. 
logger = logging.getLogger('simpleExample')


# create handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add the formatter to ch 
ch.setFormatter(formatter)

# add handler to logger
logger.addHandler(ch)

# some plenty app code 

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
