# Python XML DOM Minidom
# xml.dom.minidom — Minimal DOM implementation.
# xml.dom.minidom is a minimal implementation of the Document Object Model interface, with an API similar to that in other languages.
# It is intended to be simpler than the full DOM and also significantly smaller.
# Users who are not already proficient with the DOM should consider using the xml.etree.ElementTree module for their XML processing instead.
#
 
#
# Warning:
# The xml.dom.minidom module is not secure against maliciously constructed data.
# If you need to parse untrusted or unauthenticated data see XML vulnerabilities.
#

# 
# DOM applications typically start by parsing some XML into a DOM.
# With xml.dom.minidom, this is done through the parse functions:
# 

from xml.dom.minidom import parse, parseString

dom1 = parse('c:\\temp\\mydata.xml')  # parse an XML file by name

datasource = open('c:\\temp\\mydata.xml')
dom2 = parse(datasource)  # parse an open file

dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')
