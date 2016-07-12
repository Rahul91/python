# config.py

pwd = path.dirname(path.abspath(__file__))

LOGGING_CONFIG = dict(
    version = 1,
    formatters = {
        'compact': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'},
        'verbose': {
                'format': '%(asctime)s [%(levelname)-8.8s] %(name)-8.8s [%(filename)-15.15s:%(lineno)-3.3s]: %(message)s'
            }
        },
    handlers = {
        'default': {'class': 'logging.StreamHandler',
                    'formatter': 'compact',
                    'level': logging.DEBUG
                    },
        'api': {'class': 'logging.FileHandler',
                'formatter': 'compact',
                'filename': '%s/%s' % (pwd, '../logs/api/api.log'),
                'level': logging.DEBUG
              },
        },
    loggers = {
         'api': {
                'handlers': ['api'],
                'level': 'DEBUG',
                'propagate': False
            },
)



#logging.py

import logging

from project.config import LOGGING_CONFIG
from logging.config import dictConfig


dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()



# application.py

from project.logging import logger

logger.debug('')

