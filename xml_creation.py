import xml.etree.ElementTree as ET
from xml.dom import minidom as MD

def xml_tag(xmlData):
  item1 = ET.SubElement(xmlData, 'item')
  item1.set('name','item1')
  item1.text = 'item1abc'
  print(ET.tostring(xmlData, 'unicode', 'xml'))
  return xmlData

# create the file structure
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item1.set('name','item1')
item1.text = 'item1abc'
# item1 = ET.SubElement(i

print(ET.tostring(xml_tag(data), 'unicode', 'xml'))
# # create a new XML file with the results
mydata = ET.tostring(data, 'unicode', 'xml')
reparsed = MD.parseString(mydata)
indent_data = reparsed.toprettyxml(indent="  ")
myfile = open("items.xml", "w")
myfile.write(indent_data)
print("done")