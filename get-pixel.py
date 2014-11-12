#!/usr/bin/python

import urllib2

lat="10.0"
lon="1.0"

url="http://maps.googleapis.com/maps/api/staticmap?center={"+lat+","+lon+"}&zoom={current%20zoom%60}&size=1x1&maptype=roadmap&sensor=false"
image=urllib2.urlopen(url)
f=open("pixel.png", 'wb')
f.write(image.read())
f.close()
