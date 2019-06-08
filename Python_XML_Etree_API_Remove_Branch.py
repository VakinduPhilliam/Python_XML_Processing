# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# We can remove elements using Element.remove().
# Let’s say we want to remove all countries with a rank higher than 50:
# 

for country in root.findall('country'):
        rank = int(country.find('rank').text)

        if rank > 50:
            root.remove(country)

tree.write('output.xml')
