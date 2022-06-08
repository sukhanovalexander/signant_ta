import sys
import configparser as c
import logging
import json


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

config = c.ConfigParser()
try:
    config.read('config.ini')
    host = config['server']['url']

    token_route = config['api']['token_route']
    user_route = config['api']['user_route']
    head = config['api']['head']

except c.Error as e:
    logger.critical('Error importing configs: %'.format(e.message))
    sys.exit(1)
