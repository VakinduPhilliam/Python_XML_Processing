# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# Pull API for non-blocking parsing:
# Most parsing functions provided by this module require the whole document to be read at once before returning any result.
# It is possible to use an XMLParser and feed data into it incrementally, but it is a push API that calls methods on a callback target, which is too
# low-level and inconvenient for most needs.
# Sometimes what the user really wants is to be able to parse XML incrementally, without blocking operations, while enjoying the convenience of fully
# constructed Element objects.
# 

#
# The most powerful tool for doing this is XMLPullParser.
# It does not require a blocking read to obtain the XML data, and is instead fed with data incrementally with XMLPullParser.feed() calls.
# To get the parsed XML elements, call XMLPullParser.read_events().
#

#
# Here is an example:
# 

parser = ET.XMLPullParser(['start', 'end'])
parser.feed('<mytag>sometext')

list(parser.read_events())

# OUTPUT: '[('start', <Element 'mytag' at 0x7fa66db2be58>)]'

parser.feed(' more text</mytag>')

for event, elem in parser.read_events():
        print(event)

        print(elem.tag, 'text=', elem.text)
