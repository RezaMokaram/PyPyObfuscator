import logging

logging.basicConfig(
    format='%(levelname)s - (%(asctime)s) - %(message)s - (Line: %(lineno)d) - [%(filename)s]',
    datefmt='%H:%M:%S',
    encoding='utf-8',
    level=logging.INFO
)

