import logging
import time

def generate_log():
    # Create a logger
    logger = logging.getLogger('TestLog')
    logger.setLevel(logging.INFO)

    # Create a stream handler
    stream_handler = logging.StreamHandler()

    # Create a formatter and add it to the stream handler
    formatter = logging.Formatter('%(message)s')
    stream_handler.setFormatter(formatter)

    # Add the stream handler to the logger
    logger.addHandler(stream_handler)

    # Generate the log message
    logger.info('vault is sealed. BUT IT IS NOT REAL, JUST FOR TEST.')

    # Remove the stream handler from the logger
    logger.removeHandler(stream_handler)

if __name__ == '__main__':
    generate_log()
    time.sleep(120)
