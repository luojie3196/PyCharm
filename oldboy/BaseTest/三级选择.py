#!/usr/bin/python
# encoding:utf-8

dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "湖南": {
        "长沙": ["长沙县", "浏阳市", "望城区"],
        "衡阳": ["衡南县", "衡东县", "祁东县"],
    }
}

province_dic = {}
for key, province in enumerate(dic.keys(), 1):
    province_dic[key] = province
    print(key, province)

inp1 = input('请选择省份: ')
if not province_dic.get(int(inp1)):
    print('选择的省份不存在！')
    exit()
city_dic = {}
for key, city in enumerate(dic[province_dic[int(inp1)]].keys(), 1):
    city_dic[key] = city
    print(key, city)

inp2 = input('请选择城市：')
if not city_dic.get(int(inp2)):
    print('选择的城市不存在！')
    exit()
county_dic = {}
for key, county in enumerate(dic[province_dic[int(inp1)]][city_dic[int(inp2)]], 1):
    county_dic[key] = county
    print(key, county)

inp3 = input('请选择地区：')
if not county_dic.get(int(inp3)):
    print('选择的地区不存在！')
    exit()
print(county_dic[int(inp3)])