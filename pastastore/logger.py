import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create file handler
fh = logging.FileHandler('file.log')

# create formatter
formatter = logging.Formatter("""%(asctime)s - %(name)s - %(levelname)s - \
%(message)s""")

# add formatter to ch
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(fh)
