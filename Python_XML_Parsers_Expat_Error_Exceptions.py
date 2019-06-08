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
# ExpatError Exceptions
# ExpatError exceptions have a number of interesting attributes:
#

#
# ExpatError.code 
# Expat’s internal error number for the specific error.
# The errors.messages dictionary maps these error numbers to Expat’s error messages.
#

#
# For example:
# 

from xml.parsers.expat import ParserCreate, ExpatError, errors

p = ParserCreate()

try:
    p.Parse(some_xml_document)

except ExpatError as err:
    print("Error:", errors.messages[err.code])
