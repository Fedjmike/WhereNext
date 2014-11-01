#! /usr/bin/python

import sys
import math

# point = sys.argv[1]

# visited = sys.argv[2:]

def rad(pair):
	a=pair[0]
	b=pair[1]
	rad_a = a*math.pi/180.0
	rad_b = b*math.pi/180.0
	return [rad_a,rad_b]

def distance(a, b):
	ca = math.acos(math.sin(a[0])*math.sin(b[0])+math.cos(a[0])*math.cos(b[0])*math.cos(a[1]-b[1]))
	return ca

point=[0.0,270.0]
visited=[[0.0,0.0],[90.0,90.0]]

distances=[]
for temp_point in visited:
	distances.append(distance(rad(point),rad(temp_point)))
print min(distances)
# print distance(rad(a),rad(b))
# print distance(rad([a,b]))
