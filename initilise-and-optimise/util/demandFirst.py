import numpy as np

"""
The demand firts approach will ignore distances and look only towards the demand at each point.
low-first will travel from lowest demand to highest demand untill it's capacity is full.
"""

def demandFirst(dim, distances, capacity, demands, lowFirst=True):
    ids = list(range(1,len(demands)+1))
    tups = [(ids[i],demands[i]) for i in range(len(ids))]
    tups.pop(0)
    tups.sort(key=lambda x: x[1])
    solution = []
    while len(tups) > 0:
        demand = 0
        string = [1]
        while len(tups) > 0:
            demand += int(tups[0][1])
            if demand >= capacity:
                break
            string.append(tups[0][0])
            tups.pop(0)
        string.append(1)
        solution.append(string)
    return solution