# Python XML Parsers Expat
# xml.parsers.expat — Fast XML parsing using Expat
#
# Warning:
# The pyexpat module is not secure against maliciously constructed data.
# If you need to parse untrusted or unauthenticated data see XML vulnerabilities.
# 
# The xml.parsers.expat module is a Python interface to the Expat non-validating XML parser.
# The module provides a single extension type, xmlparser, that represents the current state of an XML parser.
# After an xmlparser object has been created, various attributes of the object can be set to handler functions.
# When an XML document is then fed to the parser, the handler functions are called for the character data and markup in the XML document.
#

#
# The following program defines three handlers that just print out their arguments.
# 

import xml.parsers.expat

# 3 handler functions

def start_element(name, attrs):
    print('Start element:', name, attrs)

def end_element(name):
    print('End element:', name)

def char_data(data):
    print('Character data:', repr(data))

p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element

p.CharacterDataHandler = char_data

p.Parse("""<?xml version="1.0"?>
<parent id="top"><child1 name="paul">Text goes here</child1>
<child2 name="fred">More text</child2>
</parent>""", 1)
