# -------------------- cs253 week 5 --------------------

import urllib
import urllib2

def sect_3_urlib():
	p = urllib2.urlopen('http://www.google.com')
	# p is like a file object in python
	c = p.read()
	# c is like content, which you read from p(the file in a sense)
	#print c
	print dir(p) #which print the directory of p(since p is like a file)
	print 'p.url: ', p.url
	print 'p.headers: ', p.headers
	print 'p.headers.items(): ', p.headers.items()
	print "p.headers['content-type']: ", p.headers['content-type']

def sect_4_using_urllib():
	p = urllib2.urlopen('http://www.example.com')
	print 'p.headers["server"]: ', p.headers["server"]

#sect_4_using_urllib()

"""
More info on working with the DOM in python:

    Minidom Documentation.
	[http://docs.python.org/library/xml.dom.minidom.html]
    Minidom Wiki Page with examples of very basic operations.
	[http://wiki.python.org/moin/MiniDom]
    For a more full-featured implementation of the DOM, try the main DOM python package.

For more information on the DOM:

    The DOM Wikipedia page.
    An Explanation of the DOM by W3.

Again, none of this is strictly necessary for this course.

"""

from xml.dom import minidom

def sect_07_parsing_xml():
	x = minidom.parseString('''
	<mytag>
		contents!
		<children>
			<item>1</item>
			<item>2</item>
		</children>
	</mytag>
	''')
	print 'x: ', x
	print 'dir(x): ', dir(x)
	print 'x.toprettyxml(): '
	print x.toprettyxml()
	print 'x.getElementsByTagName("item"): ', x.getElementsByTagName("item")
	print 'x.getElementsByTagName("item")[0]: ', x.getElementsByTagName("item")[0]
	print 'x.getElementsByTagName("item")[0].childNodes: '
	print x.getElementsByTagName("item")[0].childNodes
	print 'x.getElementsByTagName("item")[0].childNodes[0].nodeValue: '
	print x.getElementsByTagName("item")[0].childNodes[0].nodeValue

def sect_09_parsing_rss():
	p = urllib2.urlopen('http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml')
	c = p.read()
	x = minidom.parseString(c)
	ans = x.getElementsByTagName("item")
	print 'ans: ', ans
	print 'len(ans): ', len(ans)
	
import json

def sect_10_json():
	j = '{"one":1, "numbers":[1,2,3,4,5]}'
	d = json.loads(j)
	print 'd["numbers"]: ', d["numbers"]
	

# QUIZ - reddit_front is a JSON string of reddit's front page. Inside it is a
# list of links, each of which has an "ups" attribute. From this dataset, what
# is the total number of ups of all the links?
#
# Implement the function total_ups(), and make it return the total number of ups.
# This is going to require some experimental searching through the reddit_front 
# JSON, which is a fairly typical problem when dealing with APIs, RSS, or JSON. 
# You'll need to load the json using the json.loads method, after which you 
# should be able to search through the json similarly to a dictionary or list. 
# Note that you will need to access parts of the JSON as a dictionary, and 
# others as a list.
# You can also try running this in the python interpreter in the console, 
# which may make it easier to search through reddit_front.

def total_ups():
	f = open('cs253_unit05_supplement_1.txt', 'r')
	j = f.read()
	d = json.loads(j)
	total = 0
	for item in d['data']['children']:
		total += item['data']['ups']
	return total

# r"abc" means tell python to intepret "abc" as raw string

print json.dumps([1,2,3])

print json.dumps({"one": 1, "two":'the man said, "cool!"'})

print json.dumps({"blah":["one", 2, 'th"r"ee']})


xml = '''<HostipLookupResultSet xmlns:gml="http://www.opengis.net/gml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.1" xsi:noNamespaceSchemaLocation="http://www.hostip.info/api/hostip-1.0.1.xsd">
           <gml:description>This is the Hostip Lookup Service</gml:description>
           <gml:name>hostip</gml:name>
           <gml:boundedBy>
             <gml:Null>inapplicable</gml:Null>
           </gml:boundedBy>
           <gml:featureMember>
             <Hostip>
               <ip>12.215.42.19</ip>
               <gml:name>Aurora, TX</gml:name>
               <countryName>UNITED STATES</countryName>
               <countryAbbrev>US</countryAbbrev>
               <!-- Co-ordinates are available as lng,lat -->
               <ipLocation>
                 <gml:pointProperty>
                   <gml:Point srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
                     <gml:coordinates>-97.5159,33.0582</gml:coordinates>
                   </gml:Point>
                 </gml:pointProperty>
               </ipLocation>
             </Hostip>
           </gml:featureMember>
        </HostipLookupResultSet>'''

# QUIZ - implement the get_coords(xml) function that takes in an xml string 
# and returns a tuple of (lat, lon) if there are coordinates in the xml.
# Remember that you should use minidom to do this.
# Also, notice that the coordinates in the xml string are in the format:
# (lon,lat), so you will have to switch them around.

from xml.dom import minidom

def get_coords(xml):
	x = minidom.parseString(xml)
	c = x.getElementsByTagName('gml:coordinates')
	if c and c[0].childNodes[0].nodeValue:
		(lon, lat) = c[0].childNodes[0].nodeValue.split(',')
		return (lat,lon)

print get_coords(xml)

# use repr to print pythong obj in google



from collections import namedtuple

# make a basic Point class
Point = namedtuple('Point', ["lat", "lon"])
points = [Point(1,2),
          Point(3,4),
          Point(5,6)]

# implement the function gmaps_img(points) that returns the google maps image
# for a map with the points passed in. A example valid response looks like
# this:
#
# http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&markers=1,2&markers=3,4
#
# Note that you should be able to get the first and second part of an individual Point p with
# p.lat and p.lon, respectively, based on the above code. For example, points[0].lat would 
# return 1, while points[2].lon would return 6.

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false"

def gmaps_img(points):
	url = GMAPS_URL
	for point in points:
		url = url + '&markers={0},{1}'.format(point.lat, point.lon)
	return url

print gmaps_img(points)



	

