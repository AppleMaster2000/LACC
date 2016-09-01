
def main(fname):
    
    # create a world
    m = world()
    fn2 = '%s.gif' % fname
    # load the map
    print ("Loading file", fn2)
    m.create_map(fn2)
    m.read_locations('%s.loc' % (fname))
    
    # locations 
    places = m.locations.values()
    
    # rearrange the places to decrease the trip time
    places = speedyTrip(places)
    
    m.input_trip(places)
    m.win.getMouse()

visited = [False]
went = []
counter = 0
#*************************************
# This is where you write your code
# input: all locations
# output: locations (sorted)
#*************************************
def speedyTrip(places):
    # places is a list of locations
    # the first place is places[0]
    # places[0].name : name of the first place
    # places[0].x
    # x_location
    # places[0].y
    # y_location
    # get_distance(places[0], places[1]) returns 
    # the distance between places[0] and places[1]
    
    #these are random code statement that you may or may not want to use.
    cities=[]
    unvisited_cities=list(range(0,52))
    visited_cities=[0]
    print (visited_cities)
    print (unvisited_cities)    
    unvisited_cities.remove(0)
    next_city= unvisited_cities[0]

    distance2 = [range(0,53)]
    
    for x in range(0,52):
        distance = [0,53]
        max = 10000
        for i in range(1,52):
            if(len(distance) == 51):
                distance.sort
                distance2[x] = distance[x]
                print(str(distance2))
            else:
                distance.append(get_distance(places[x], places[i + 1]))
        

    visited_cities.append(next_city)
    unvisited_cities.remove(next_city)
    print (visited_cities)
    return places

if __name__ == "__main__":
    import sys
    import re
    from graphics import *
    from tools import *
    main("usa")
    
