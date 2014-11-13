# x,y range from -1 to 1

import math

# truncating at this latitude gives an aspect ratio of 1 (used by Google Maps)
lat_lim=math.atan(math.sinh(math.pi))*180.0/math.pi

# x,y have limits of -1,1
def geo_to_world(geo_pair):
	lat=geo_pair[0]
	lon=geo_pair[1]
	x=lon/180.0
	y=math.log(math.tan(math.pi/4.0+math.pi*lat/360.0))/(math.log(math.tan(math.pi/4.0+lat_lim*math.pi/360.0)))
	return [x,y]

# lat,long have limits of [-90,90],[-180,180] (not quite for lat since we can't represent anything outside of lat_lim )
def world_to_geo(world_pair):
	x=world_pair[0]
	y=world_pair[1]
	lon=x*180.0
	lat=(math.atan(math.exp(y*math.log(math.tan(math.pi/4.0+lat_lim*math.pi/360.0))))-math.pi/4.0)*360.0/math.pi
	return [lat,lon]

def world_to_pixel(world_pair):
	x=int(512.0*(1.0+world_pair[0]))
	y=int(512.0*(1.0-world_pair[1]))
	return [x,y]
	