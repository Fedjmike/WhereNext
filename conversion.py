# x,y range from -1 to 1

import math

lat_lim=85.0

def geo_to_world(pair):
	lat=pair[0]
	lon=pair[1]
	x=lon/180.0
	y=math.log(math.tan(math.pi/4.0+math.pi*lat/360.0))/(math.log(math.tan(math.pi/4.0+lat_lim*math.pi/360.0)))
	return [x,y]

def world_to_geo(pair):
	x=pair[0]
	y=pair[1]
	lon=x*180.0
	lat=(math.atan(math.exp(y*math.log(math.tan(math.pi/4.0+lat_lim*math.pi/360.0))))-math.pi/4.0)*360.0/math.pi
	return [lat,lon]

print world_to_geo(geo_to_world([45,45]))
	