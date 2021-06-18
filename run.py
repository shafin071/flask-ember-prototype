import logging
from app import *


logging.getLogger(__name__)

logging.basicConfig(
    format='%(levelname)-8s %(asctime)-15s %(process)4d:%(threadName)-11s %(name)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG
)


if __name__ == '__main__':
    try:
        app.run()
    except Exception as ex:
        logging.error(ex)