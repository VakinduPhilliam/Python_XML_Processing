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
# DOM Objects:
# 
# The definition of the DOM API for Python is given as part of the xml.dom module documentation.
# This section lists the differences between the API and xml.dom.minidom.
#
# Node.unlink() 
# Break internal references within the DOM so that it will be garbage collected on versions of Python without cyclic GC.
# Even when cyclic GC is available, using this can make large amounts of memory available sooner, so calling this on DOM objects as soon as they are no
# longer needed is good practice.
# This only needs to be called on the Document object, but may be called on child nodes to discard children of that node.
#

# 
# You can avoid calling this method explicitly by using the with statement.
# The following code will automatically unlink dom when the with block is exited:
# 

with xml.dom.minidom.parse(datasource) as dom:

             # Work with dom.
