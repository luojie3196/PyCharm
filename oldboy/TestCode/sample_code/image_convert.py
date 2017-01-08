#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageFilter


img = Image.open('logo.jpg')
# img.show()
print(img.size, img.format, img.mode)

img_new = img.filter(ImageFilter.BLUR)
img_new.show()

# "L", "RGB" and "CMYK."
# convert = img.convert('L')
# convert.show()

# 旋转某个角度
# retot = img.rotate(90)
# retot.show()
# print img.load()
# r,g,b = img.split()
# print(r,g,b)
# r.show()
# g.show()
# b.show()
# img_new = Image.merge('RGB', (r,g,b))
# img_new.show()

# 截取指定区域
# box = (0, 0 , 500, 500)
# region = img.crop(box)
# print region.show()
# region.save('test.jpg')

# 旋转某个角度
# region = region.transpose(Image.ROTATE_90)
# print region.show()

# Pastes another image into this image
# img.paste(region, box)
# print img.show()

# img.show()
# out = img.resize((128, 128))
# out.show()
out = img.transpose(Image.FLIP_LEFT_RIGHT)       #左右对换
# out.show()
out = img.transpose(Image.FLIP_TOP_BOTTOM)       #上下对换