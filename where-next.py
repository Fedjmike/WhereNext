from Tkinter import *
import geocoder
from pygeocoder import Geocoder
from pygeolib import GeocoderError

import itertools
import operator
from math import *

import colorsys

from conversion import *
from geomaths import *

scale_linear = operator.div
scale_log = log
    
def colour_red(value):
    return (255*value, 0, 0)
    
def colour_bluewhite(value):
    value *= 255
    return (255-value, 255-value, 255)
    
def colour_contour(value):
    closeness = 0.04
    invcloseness = 1/closeness
    closeness_ = closeness*0.1

    frac = round(value*10)-value*10
    dist = abs(frac)
    
    if dist >= closeness or value < closeness_:
        return (255, 255, 255)
        
    else:
        return (dist*255*invcloseness, dist*255*invcloseness, dist*255*invcloseness)
    
def colour_hue(value):
    return tuple(map(lambda x: x*255, colorsys.hsv_to_rgb(0.8*value, 1.0, 1.0)))

def compose_colours(colour, scale):
    return lambda x, y: colour(scale(x, y))
    
###

def frange(start, end, step):
    assert(step != 0)
    sample_count = (end - start) / step
    return lambda: itertools.islice(itertools.count(start, step), sample_count)

num = 800.0

def compute(visited, width, height):
    x_range = frange(0.0, 1.0, 1.0/num)
    y_range = frange(0.0, 1.0, 1.0/num)
    distances = [[0 for x in x_range()] for y in y_range()]
    largest = 0
    largest_at = (0.0, 0.0)
    
    for x in x_range():
        print x
        for y in y_range():
            point = webm_to_geo([x, y])
            distance = min_distance(point, visited)
            distances[int(num*x)][int(num*y)] = distance
            
            #Largest yet?
            if distance > largest:
                largest = distance
                largest_at = point
                
    return distances, largest, largest_at
    
def blit(image, x, y, colour):
    hex_colour = "#%02x%02x%02x" % colour
    image.put(hex_colour, to=(x, y))

def plot(distances, largest, width, height, cfunction):
    image = PhotoImage(width=width, height=height)

    for x in xrange(0, len(distances)):
        for y in xrange(0, len(distances[x])):
            colour = cfunction(distances[x][y], largest)
            blit(image, x, int(num)-y, colour)
            
    return image

###

width = 800
height = 800
colourf = compose_colours(colour_red, scale_linear)

###

visited_strings = ["moscow"]
visited = [(location.lat, location.lng) for location in [geocoder.google(place) for place in visited_strings]]

print visited

distances, largest, largest_at = compute(visited, width, height)

try:
    print "You should travel to %s which is %d km away from anywhere you have been." % (Geocoder.reverse_geocode(*largest_at)[0], largest)
    
except GeocoderError:
    print "You should travel to %s which is %d km away from anywhere you have been." % (largest_at, largest)

###
    
root = Tk()
root.title("WhereNext")

image = plot(distances, largest, width, height, colourf)

label = Label(root, image=image)
label.pack()

try:
    root.mainloop()
    
except KeyboardInterrupt:
    pass
