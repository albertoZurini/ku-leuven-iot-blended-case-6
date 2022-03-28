import numpy as np
import math

"""
The radial pathfinding approach focusses on minimising paths not radial from the center point.
In other words, only try to move out or in the direction of the depot.
This is achieved by deviding all points in sections of the pie with each a demand less than the max capacity.
From these pie sections, a greedy algorithm will find a naieve solution within the pie-slice.
"""

def getRads(x, y, depot):
    rads = [361]  
    for i in range(1,len(x)):
        rads.append(getRadial(int(depot[0]),int(depot[1]),int(x[i]),int(y[i])))
    return rads

def getRadial(x1,y1,x2,y2):
    x = x2 - x1
    y = y2 - y1
    t = math.atan(y/(x+0.01))*180/math.pi
    if x < 0:
        t += 180
    if t < 0:
        t += 360
    return round(t)

def radial(depot, x, y, capacity, demands, rads, calc_dist):
    strings = []
    i=0
    while i < len(rads) - 1:
        
        # get trucks per pie-slice
        demand = 0
        pop = []
        while i < len(rads) - 1:
            radindex = np.argmin(rads)
            demand += int(demands[radindex])
            if demand > capacity:
                break
            pop.append(int(radindex+1))
            rads[radindex] = 1000
    
            i += 1
        
        #get optimal path per truck (greedy)
        distances = [round(calc_dist((int(depot[0]),int(depot[1])),(int(x[idx-1]),int(y[idx-1])))) for idx in pop]
        
        string = [1]
        while len(pop) > 0:
            nodeix = np.argmin(distances)
            string.append(pop[nodeix])
            distances.pop(nodeix)
            pop.pop(nodeix)
        string.append(1)
        strings.append(string)
    
    return strings