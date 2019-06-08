# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# We can import XML Data (country_data.xml) by reading from a file:
# 

import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')

root = tree.getroot()

# 
# Or directly from a string:
# 

root = ET.fromstring(country_data_as_string)

# 
# fromstring() parses XML from a string directly into an Element, which is the root element of the parsed tree.
# Other parsing functions may create an ElementTree.
#

# 
# As an Element, root has a tag and a dictionary of attributes:
# 

root.tag

# OUTPUT: 'data'

root.attrib

# OUTPUT: '{}'

# 
# It also has children nodes over which we can iterate:
# 

for child in root:
        print(child.tag, child.attrib)

#
# Children are nested, and we can access specific child nodes by index:
# 

root[0][1].text

# OUTPUT: '2008'
