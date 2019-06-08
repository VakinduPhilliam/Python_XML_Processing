# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# An example that demonstrates some of the XPath capabilities of the module.
# We’ll be using the countrydata XML document from the Parsing XML section:
# 

import xml.etree.ElementTree as ET

root = ET.fromstring(countrydata)

# Top-level elements

root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements

root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child

root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'

root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent

root.findall(".//neighbor[2]")
