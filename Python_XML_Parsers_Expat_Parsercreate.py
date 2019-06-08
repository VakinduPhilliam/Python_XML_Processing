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
# xml.parsers.expat.ParserCreate(encoding=None, namespace_separator=None): 
# Creates and returns a new xmlparser object. encoding, if specified, must be a string naming the encoding used by the XML data.
# Expat doesn’t support as many encodings as Python does, and its repertoire of encodings can’t be extended; it supports UTF-8, UTF-16, ISO-8859-1 (Latin1),
# and ASCII.
# If encoding is given it will override the implicit or explicit encoding of the document.
#

# 
# Expat can optionally do XML namespace processing for you, enabled by providing a value for namespace_separator.
# The value must be a one-character string; a ValueError will be raised if the string has an illegal length (None is considered the same as omission).
# When namespace processing is enabled, element type names and attribute names that belong to a namespace will be expanded.
# The element name passed to the element handlers StartElementHandler and EndElementHandler will be the concatenation of the namespace URI, the namespace
# separator character, and the local part of the name.
# If the namespace separator is a zero byte (chr(0)) then the namespace URI and the local part will be concatenated without any separator.
#

# 
# For example, if namespace_separator is set to a space character (' ') and the following document is parsed:
# 

#
# <?xml version="1.0"?>
# <root xmlns    = "http://default-namespace.org/"
#      xmlns:py = "http://www.python.org/ns/">
#  <py:elem1 />
#  <elem2 xmlns="" />
# </root>
# 

#
# StartElementHandler will receive the following strings for each element:
# 

#
# http://default-namespace.org/ root
# http://www.python.org/ns/ elem1
# elem2
#