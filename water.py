from conversion import *
import pickle

# map generated using a staticmap query
# http://maps.googleapis.com/maps/api/staticmap?scale=2&center=0.0,-0.0&zoom=1&size=512x512&sensor=false&visual_refresh=true&style=feature:water|color:0x00FF00&style=element:labels|visibility:off&style=feature:transit|visibility:off&style=feature:poi|visibility:off&style=feature:road|visibility:off&style=feature:administrative|visibility:off
# .csv file generated from the map
filename = "map.csv"
water_colour = (0, 255, 0)

f=open(filename,'rb')
pixel=pickle.load(f)

# takes a (lat,lon) pair and returns whether or not the spot is water
def is_water(geo_pair):
	if geo_pair[0]>85.0:
		return 1
	webm_pair=geo_to_webm(geo_pair)
	[pix_x,pix_y]=webm_to_pixel(webm_pair)
	if pixel[pix_y][pix_x]==1:
		return 1
	else:
		return 0