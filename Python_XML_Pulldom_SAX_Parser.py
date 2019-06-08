# Python XML Pulldom
# xml.dom.pulldom — Support for building partial DOM trees.
# The xml.dom.pulldom module provides a “pull parser” which can also be asked to produce DOM-accessible fragments of the document where necessary.
# The basic concept involves pulling “events” from a stream of incoming XML and processing them.
# In contrast to SAX which also employs an event-driven processing model together with callbacks, the user of a pull parser is responsible for explicitly
# pulling events from the stream, looping over those events until either processing is finished or an error condition occurs.
#

#
# The SAX parser no longer processes general external entities by default to increase security by default.
# To enable processing of external entities, pass a custom parser instance in:
# 

from xml.dom.pulldom import parse
from xml.sax import make_parser
from xml.sax.handler import feature_external_ges

parser = make_parser()
parser.setFeature(feature_external_ges, True)

parse(filename, parser=parser)

# 
# Example:
# 

from xml.dom import pulldom

doc = pulldom.parse('sales_items.xml')

for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'item':

        if int(node.getAttribute('price')) > 50:
            doc.expandNode(node)

            print(node.toxml())
