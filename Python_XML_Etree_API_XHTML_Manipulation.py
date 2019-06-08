# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# Example of changing the attribute “target” of every link in first paragraph:
# 

from xml.etree.ElementTree import ElementTree

tree = ElementTree()
tree.parse("index.xhtml")

# OUTPUT: '<Element 'html' at 0xb77e6fac>'

p = tree.find("body/p")     # Finds first occurrence of tag p in body
p

# OUTPUT: '<Element 'p' at 0xb77ec26c>'

links = list(p.iter("a"))   # Returns list of all links
links

# OUTPUT: '[<Element 'a' at 0xb77ec2ac>, <Element 'a' at 0xb77ec1cc>]'

for i in links:             # Iterates through all found links
        i.attrib["target"] = "blank"

tree.write("output.xhtml")
