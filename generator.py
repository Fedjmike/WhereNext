import PIL
import Image
import pickle
# map generated using a staticmap query
# http://maps.googleapis.com/maps/api/staticmap?scale=2&center=0.0,-0.0&zoom=1&size=512x512&sensor=false&visual_refresh=true&style=feature:water|color:0x00FF00&style=element:labels|visibility:off&style=feature:transit|visibility:off&style=feature:poi|visibility:off&style=feature:road|visibility:off&style=feature:administrative|visibility:off
# outputs a .csv file with 1 for 'water and 0 for 'no water'
filename = "map.png"
water_colour = (0, 255, 0)

def is_water():
	img=Image.open(filename).convert('RGB')
	pixel=img.load()
	arr=[]
	for y in xrange(0,1024):
		print y
		arr.append([])
		for x in xrange(0,1024):
			if pixel[x,y]==water_colour:
				arr[y].append(1)
			else:
				arr[y].append(0)
	result = open("newfile.csv",'wb')
	pickle.dump(arr,result)
is_water()