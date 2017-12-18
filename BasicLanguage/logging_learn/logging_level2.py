# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import logging

#create logger
logger = logging.getLogger('Logingtest_level2')
logger.setLevel(logging.WARNING)


# create console handler and set level to debug
ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)

# create file handler and set level to warning
fh = logging.FileHandler("access.log")
# fh.setLevel(logging.ERROR)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')