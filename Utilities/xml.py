import xml.etree.ElementTree as ET

def print_xml_file(filename):
  tree = ET.parse(filename)
  root = tree.getroot()
  
  ET.indent(root)
  print(ET.tostring(root, encoding='unicode'))
