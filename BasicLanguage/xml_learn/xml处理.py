# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import xml.etree.ElementTree as ET

tree = ET.parse("xml.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print(child.tag, child.attrib)#打印标签名和属性
    for i in child:
        print(i.tag,i.text)#打印子标签的标签名和内容

#只遍历year 节点
for node in root.iter('year'):#递归的进行查找，查找标签名为year的标签
    print(node.tag,node.text)