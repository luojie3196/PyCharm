#!/usr/bin/env python
# -*- coding:gbk -*-

import sys
print(sys.getdefaultencoding())

name='���'
print(name.encode('GBK'))
print(name.encode('utf-8'))
print(str(name.encode('utf-8'), encoding='utf-8'))
print(str(name.encode('GBK').decode('GBK')))