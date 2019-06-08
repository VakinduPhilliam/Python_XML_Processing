# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# Search and Explore XML Document
#

#
# One way to search and explore this XML example is to manually add the URI to every tag or attribute in the xpath of a find() or findall():
# 

root = fromstring(xml_text)

for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')

    print(name.text)

    for char in actor.findall('{http://characters.example.com}character'):

             print(' |-->', char.text)
 
#
# A better way to search the namespaced XML example is to create a dictionary with your own prefixes and use those in the search functions:
# 

ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)

    print(name.text)

    for char in actor.findall('role:character', ns):

              print(' |-->', char.text)
