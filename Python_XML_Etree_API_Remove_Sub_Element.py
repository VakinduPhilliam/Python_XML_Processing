# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# remove(subelement) 
# Removes subelement from the element.
# Unlike the find* methods this method compares elements based on the instance identity, not on tag value or contents.
#

# 
# Element objects also support the following sequence type methods for working with subelements: __delitem__(), __getitem__(), __setitem__(), __len__().
#

# 
# Caution: Elements with no subelements will test as False.
# This behavior will change in future versions. Use specific len(elem) or elem is None test instead.
# 

element = root.find('foo')

if not element:  # careful!
    print("element not found, or element has no subelements")

if element is None:
    print("element not found")
