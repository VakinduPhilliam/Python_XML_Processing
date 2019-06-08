# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# Modifying an XML File:
# ElementTree provides a simple way to build XML documents and write them to files.
# The ElementTree.write() method serves this purpose.
#

# 
# Once created, an Element object may be manipulated by directly changing its fields (such as Element.text), adding and modifying attributes (Element.set()
# method), as well as adding new children (for example with Element.append()).
#

# 
# Let’s say we want to add one to each country’s rank, and add an updated attribute to the rank element:
# 

for rank in root.iter('rank'):
        new_rank = int(rank.text) + 1
        rank.text = str(new_rank)

        rank.set('updated', 'yes')

tree.write('output.xml')
