# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import xml.etree.ElementTree as ET

tree = ET.parse("xml.xml")
root = tree.getroot()

#修改year节点的内容，使年份+1，并设置year节点属性，updated=yes
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated","yes")

#保存修改的xml文件
tree.write("xmltest.xml")


#删除node
#删除排名大于50的country节点
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)

tree.write('output.xml')