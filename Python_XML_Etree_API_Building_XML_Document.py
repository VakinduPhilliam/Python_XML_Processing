# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# Building XML documents:
# The SubElement() function also provides a convenient way to create new sub-elements for a given element:
# 

a = ET.Element('a')
b = ET.SubElement(a, 'b')

c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')

ET.dump(a)

# OUTPUT: '<a><b /><c><d /></c></a>'
