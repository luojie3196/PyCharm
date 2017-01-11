#!/usr/bin/python
# encoding:utf-8

import jieba

# 中文分词
# 全模式
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
seg_list = jieba.cut("李克强在国家科学技术奖励大会上的讲话", cut_all=True)
print("Full Mode: ", ",".join(seg_list))

# 精确模式
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
seg_list = jieba.cut("李克强在国家科学技术奖励大会上的讲话", cut_all=False)
print("Default Mode: ", ",".join(seg_list))

# 默认是精确模式
# seg_list = jieba.cut("今天天气很好适合外出爬山")
seg_list = jieba.cut("李克强在国家科学技术奖励大会上的讲话")
print(",".join(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search("李克强在国家科学技术奖励大会上的讲话")
print(",".join(seg_list))


# 关键词提取
print("#" * 40)
import jieba.analyse

# 基于TF-IDF
sentence = "李克强在国家科学技术奖励大会上的讲话"
seg_list = jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
print(",".join(seg_list))

# 基于TextRank
seg_list = jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
print(",".join(seg_list))

# 词性标注
import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s, %s' % (word, flag))
