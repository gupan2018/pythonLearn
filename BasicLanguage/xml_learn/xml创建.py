# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import xml.etree.ElementTree as ET

#设置根节点
new_xml = ET.Element("namelist")
#设置"namelist"的子节点以及属性
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text = '33'
name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
#设置name的子节点以及属性和内容
age = ET.SubElement(name2,"age")
age.text = '19'

#生成文档对象
et = ET.ElementTree(new_xml)
#写入xml文件
et.write("test.xml", encoding="utf-8",xml_declaration=True)

ET.dump(new_xml) #打印生成的格式