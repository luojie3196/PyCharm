#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging


# logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.critical("server is down")

# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log', level=logging.INFO)
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log', level=logging.INFO)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')


# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('is when this event was logged.')


# create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
fh = logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)
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
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')



# 文件自动截断例子
# from logging import handlers
#
# logger = logging.getLogger(__name__)
#
# log_file = "timelog.log"
# #fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3)
# fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S",interval=5,backupCount=3)
#
#
# formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')
#
# fh.setFormatter(formatter)
#
# logger.addHandler(fh)
#
#
# logger.warning("test1")
# logger.warning("test12")
# logger.warning("test13")
# logger.warning("test14")



