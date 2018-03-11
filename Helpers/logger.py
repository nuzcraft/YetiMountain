# this file handles logging to the output file of my choosing
import logging

# set the name of the file, the logging level, and that we want to truncate each time
logging.basicConfig(filename='ym.log', level=logging.DEBUG,
                    filemode='w')


def log(severity, message):
    # passing in the severity helps us tell the logger what to write
    if severity.lower() == 'debug':
        logging.debug(message)
    elif severity.lower() == 'info':
        logging.info(message)
    elif severity.lower() == 'warning':
        logging.warning(message)
    elif severity.lower() == 'error':
        logging.error(message)
    elif severity.lower() == 'critical':
        logging.critical(message)
    else:
        logging.warning('incorrect severity specified: ' + severity)
        logging.warning(message)

