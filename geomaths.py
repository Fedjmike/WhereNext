#! /usr/bin/python

import sys
import math

# converts coordinates from degrees to radians
def rad(pair):
	a=pair[0]
	b=pair[1]
	rad_a = a*math.pi/180.0
	rad_b = b*math.pi/180.0
	return [rad_a,rad_b]
# given a pair of coordinats, returns the geodesic distance between the two points
def distance(a, b):
	ca = math.acos(math.sin(a[0])*math.sin(b[0])+math.cos(a[0])*math.cos(b[0])*math.cos(a[1]-b[1]))
	d=6371.0*ca
	return d

def min_distance(point,visited):
	distances=[]
	for temp_point in visited:
		distances.append(distance(rad(point),rad(temp_point)))
	return min(distances)