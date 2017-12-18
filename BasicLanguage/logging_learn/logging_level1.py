# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# import logging
#
# logging.basicConfig(filename='example.log',level=logging.INFO)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

import logging
logging.basicConfig(format='%(asctime)s FILENAME:%(pathname)s LINENO:%(lineno)d %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')