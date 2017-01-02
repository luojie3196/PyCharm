#!/usr/bin/python
# encoding:utf-8

# import logging

# logging.basicConfig(filename='example.log', level=logging.INFO)
# logging.debug("This is debug info to test logging module")
# logging.info("This is info info to test logging module")
# logging.warning("This is warning info to test logging module")

import logging

# create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)  # 全局优先级最高

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