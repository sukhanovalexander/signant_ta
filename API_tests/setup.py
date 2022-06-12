import sys
import configparser as c
import logging
import json
#from variables import users as u

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

config = c.ConfigParser()
try:
    config.read(['config.ini', '../config.ini'])  # do not like this part, needs to be refactored. configparser does not
    host = config['server']['url']  # see config.ini when executing test. Possible solution from_root module

    token_route = config['api']['token_route']
    user_route = config['api']['user_route']
    head = json.loads(config['api']['head'])
#    users = u

except c.Error:
    logger.critical('Error importing configs')
    sys.exit(1)
except json.JSONDecodeError as e:
    logger.critical('Error parsing JSON : {}'.format(e))
    sys.exit(1)
except OSError:
    logger.critical('Config/JSON files missing')
    sys.exit(1)


if __name__ == '__main__':

    print(head)
