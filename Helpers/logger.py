# this file handles logging to the output file of my choosing
import logging

# set the name of the file, the logging level, and that we want to truncate each time
logging.basicConfig(filename='ym.log', level=logging.DEBUG,
                    filemode='w')


def log(severity, message):
    # passing in the severity helps us tell the logger what to write
    if severity.lower() == 'debug':
        logging.getLogger().debug(message, exc_info=False)
    elif severity.lower() == 'info':
        logging.info(message)
    elif severity.lower() == 'warning':
        logging.warning(message)
    elif severity.lower() == 'error':
        logging.getLogger().error(message, exc_info=True)
    elif severity.lower() == 'critical':
        logging.getLogger().critical(message, exc_info=True)
    else:
        logging.warning('incorrect severity specified: ' + severity)
        logging.warning(message)

