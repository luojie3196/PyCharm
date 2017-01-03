#!/usr/bin/python
# encoding:utf-8

import re
import json

characters = []
stat = {}
fr = open("xyj.txt", "r", encoding="utf-8")
for line in fr:
    line = line.strip()
    # 过滤空白行
    if len(line) == 0:
        continue
    for x in range(0, len(line)):
        # 过滤掉所有非中文字符
        if not re.match(u'[\u4e00-\u9fa5]+', line[x]):
            continue
        if line[x] not in characters:
            characters.append(line[x])
        if line[x] not in stat:
            stat[line[x]] = 0
        stat[line[x]] += 1
fr.close()
print(len(characters))
print(len(stat))
# 所得结果以jason格式存储
fw = open("result.json", "w")
fw.write(json.dumps(stat))
fw.close()
# 按value从大到小排序
stat = sorted(stat.items(), key=lambda d: d[1], reverse=True)
# 所得结果以csv格式存储
fw = open("result.csv", "w")
for x in range(0, len(stat)):
    fw.write(stat[x][0] + ":" + str(stat[x][1]) + "\n")
fw.close()
# 打印前20个字符
# for x in range(0, 20):
#     print(characters[x])
#
# print("*"*20)
# 打印排序后前20个字符的数量
# for x in range(0, 20):
#     print(stat[x][0], stat[x][1])
