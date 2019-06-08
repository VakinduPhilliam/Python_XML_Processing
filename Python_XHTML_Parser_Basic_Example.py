# Python XHTML Parser
# html.parser — Simple HTML and XHTML parser
# This module defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML (HyperText Mark-up Language) and XHTML.
#

#
# The following class implements a parser that will be used to illustrate more examples:
# 

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)

        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])

        print("Named ent:", c)

    def handle_charref(self, name):

        if name.startswith('x'):
            c = chr(int(name[1:], 16))

        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
 
#
# Parsing a doctype:
# 

parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                '"http://www.w3.org/TR/html4/strict.dtd">')

#
# Parsing an element with a few attributes and a title:
# 

parser.feed('<img src="python-logo.png" alt="The Python logo">')

parser.feed('<h1>Python</h1>')

#
# The content of script and style elements is returned as is, without further parsing:
# 

parser.feed('<style type="text/css">#python { color: green }</style>')

parser.feed('<script type="text/javascript">'
                'alert("<strong>hello!</strong>");</script>')

#
# Parsing comments:
# 

parser.feed('<!-- a comment -->'
                '<!--[if IE 9]>IE-specific content<![endif]-->')

#
# Parsing named and numeric character references and converting them to the correct char (note: these 3 references are all equivalent to '>'):
# 

parser.feed('&gt;&#62;&#x3E;')

# 
# Feeding incomplete chunks to feed() works, but handle_data() might be called more than once (unless convert_charrefs is set to True):
# 

for chunk in ['<sp', 'an>buff', 'ered ', 'text</s', 'pan>']:
        parser.feed(chunk)

#
# Parsing invalid HTML (e.g. unquoted attributes) also works:
# 

parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
