import geocoder

from geomaths import *

def compute(visited, width, height):
    largest = 0
    largest_at = (0.0, 0.0)
    
    for lat in xrange(-180, 180):
        for lng in xrange(-90, 90):
            point = (lat, lng)
            distance = min_distance(point, visited)
            
            #Largest yet?
            if distance > largest:
                largest = distance
                largest_at = point
                
    return largest, largest_at
    
###

width = 500
height = 500

###

#Google switching latitude and longitude?
visited_strings = ["15 Avondale Avenue, East Barnet"]
visited = [(location.lng, location.lat) for location in [geocoder.google(place) for place in visited_strings]]

largest, largest_at = compute(visited, width, height)

print largest_at
y, x = largest_at
largest_at = x, y
print "You should travel to %s which is %d km away from anywhere you have been." % (geocoder.google(largest_at, reverse=True).address, largest)
