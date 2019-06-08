# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# Finding interesting elements:
# 
# Element has some useful methods that help iterate recursively over all the sub-tree below it (its children, their children, and so on).
#

#
# For example, Element.iter():
# 

for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)

#
# OUTPUT:
#
# {'name': 'Austria', 'direction': 'E'}
# {'name': 'Switzerland', 'direction': 'W'}
# {'name': 'Malaysia', 'direction': 'N'}
# {'name': 'Costa Rica', 'direction': 'W'}
# {'name': 'Colombia', 'direction': 'E'}
#
 
#
# Element.findall() finds only elements with a tag which are direct children of the current element.
# Element.find() finds the first child with a particular tag, and Element.text accesses the element’s text content.
# Element.get() accesses the element’s attributes:
# 

for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')

        print(name, rank)

#
# OUTPUT:
#
# Liechtenstein 1
# Singapore 4
# Panama 68
#