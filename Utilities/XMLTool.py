import xml.etree.ElementTree as ET

class XLMTool():
  """ XML Helper Class """
  def __init__(self):
    pass

  def print_xml_file(self, filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    ET.indent(root)
    print(ET.tostring(root, encoding='unicode'))

  def getXMLS():
    xmlns = ''
    m = re.search('{.*}', root.tag)
    if m:
        xmlns = m.group(0)
