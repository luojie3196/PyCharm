#!/usr/bin/python
# -*- coding:utf-8 -*-


import xml.etree.ElementTree as ET


tree = ET.parse('test.xml')
print(tree)
root = tree.getroot()
print(root)

for child in root:
    print(child.tag, child.attrib)
    for n in child:
        # print(n.tag, n.text)
        if n.attrib:
            print(n.attrib)
        if n.text:
            print(n.text)

#只遍历year 节点
for node in root.iter('year'):
    print(node.tag,node.text)

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")

tree.write("test_new.xml")

for node in root.iter('gdppc'):
    node.text = str(int(node.text) + 1)
    node.set('updated', 'yes')

tree.write("test_new1.xml")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
age.text = '33'
sex.text = 'male'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test1.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式