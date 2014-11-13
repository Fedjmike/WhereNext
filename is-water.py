from conversion import *
import PIL
import Image

# map generated using a staticmap query
# http://maps.googleapis.com/maps/api/staticmap?scale=2&center=0.0,-0.0&zoom=1&size=512x512&sensor=false&visual_refresh=true&style=feature:water|color:0x00FF00&style=element:labels|visibility:off&style=feature:transit|visibility:off&style=feature:poi|visibility:off&style=feature:road|visibility:off&style=feature:administrative|visibility:off
filename = "map.png"
water_colour = (0, 255, 0)

def is_water(geo_pair):
	world_pair=geo_to_world(geo_pair)
	[pix_x,pix_y]=world_to_pixel(world_pair)
	img=Image.open(filename).convert('RGB')
	pixel=img.load()
	if pixel[pix_x,pix_y]==water_colour:
		return 1
	else:
		return 0
		
print is_water([-72.0,0.0])