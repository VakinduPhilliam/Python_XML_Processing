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
# You can also create a Document by calling a method on a “DOM Implementation” object.
# You can get this object either by calling the getDOMImplementation() function in the xml.dom package or the xml.dom.minidom module.
# Once you have a Document, you can add child nodes to it to populate the DOM:
# 

from xml.dom.minidom import getDOMImplementation

impl = getDOMImplementation()

newdoc = impl.createDocument(None, "some_tag", None)

top_element = newdoc.documentElement
text = newdoc.createTextNode('Some textual content.')

top_element.appendChild(text)

# 
# Once you have a DOM document object, you can access the parts of your XML document through its properties and methods.
# These properties are defined in the DOM specification.
# The main property of the document object is the documentElement property.
# It gives you the main element in the XML document: the one that holds all others.
#

#
# Here is an example program:
# 

dom3 = parseString("<myxml>Some data</myxml>")

assert dom3.documentElement.tagName == "myxml"
