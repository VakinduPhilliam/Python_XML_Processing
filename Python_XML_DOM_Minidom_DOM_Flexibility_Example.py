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
# This example program is a fairly realistic example of a simple program.
# In this particular case, we do not take much advantage of the flexibility of the DOM.
# 

import xml.dom.minidom

document = """\
<slideshow>
<title>Demo slideshow</title>
<slide><title>Slide title</title>
<point>This is a demo</point>
<point>Of a program for processing slides</point>
</slide>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>
</slideshow>
"""

dom = xml.dom.minidom.parseString(document)

def getText(nodelist):
    rc = []

    for node in nodelist:

        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)

    return ''.join(rc)

def handleSlideshow(slideshow):
    print("<html>")

    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")

    handleToc(slides)
    handleSlides(slides)

    print("</html>")

def handleSlides(slides):
    for slide in slides:

        handleSlide(slide)

def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])

    handlePoints(slide.getElementsByTagName("point"))

def handleSlideshowTitle(title):
    print("<title>%s</title>" % getText(title.childNodes))

def handleSlideTitle(title):
    print("<h2>%s</h2>" % getText(title.childNodes))

def handlePoints(points):
    print("<ul>")

    for point in points:
        handlePoint(point)

    print("</ul>")

def handlePoint(point):
    print("<li>%s</li>" % getText(point.childNodes))

def handleToc(slides):

    for slide in slides:
        title = slide.getElementsByTagName("title")[0]

        print("<p>%s</p>" % getText(title.childNodes))

handleSlideshow(dom)
