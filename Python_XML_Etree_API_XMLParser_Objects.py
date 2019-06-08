# Python XML Etree API
# xml.etree.ElementTree — The ElementTree XML API
# The xml.etree.ElementTree module implements a simple and efficient API for parsing and creating XML data.
#

#
# XMLParser Objects:
#
# class xml.etree.ElementTree.XMLParser(html=0, target=None, encoding=None): 
# This class is the low-level building block of the module.
# It uses xml.parsers.expat for efficient, event-based parsing of XML.
# It can be fed XML data incrementally with the feed() method, and parsing events are translated to a push API - by invoking callbacks on the target object.
# If target is omitted, the standard TreeBuilder is used.
# The html argument was historically used for backwards compatibility and is now deprecated.
# If encoding is given, the value overrides the encoding specified in the XML file.
#

#
# feed(data): 
# Feeds data to the parser. data is encoded data.
# 

#
# XMLParser.feed() calls target’s start(tag, attrs_dict) method for each opening tag, its end(tag) method for each closing tag, and data is processed by
# method data(data).
# XMLParser.close() calls target’s method close().
# XMLParser can be used not only for building a tree structure.
#

#
# This is an example of counting the maximum depth of an XML file:
# 

from xml.etree.ElementTree import XMLParser

class MaxDepth:                     # The target object of the parser
        maxDepth = 0

        depth = 0

        def start(self, tag, attrib):   # Called for each opening tag.
            self.depth += 1

            if self.depth > self.maxDepth:
                self.maxDepth = self.depth

        def end(self, tag):             # Called for each closing tag.
            self.depth -= 1

        def data(self, data):
            pass            # We do not need to do anything with data.

        def close(self):    # Called when all data has been parsed.
            return self.maxDepth

target = MaxDepth()
parser = XMLParser(target=target)

exampleXml = """
    <a>
      <b>
      </b>
      <b>
        <c>
          <d>
          </d>
        </c>
      </b>
    </a>"""

parser.feed(exampleXml)

parser.close()

# OUTPUT: '4'
