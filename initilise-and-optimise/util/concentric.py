import numpy as np

"""
Similarly to the greedy algorithm, theh concentric approach will select the local optimal solution at each step.
But it will only look at distances from the depot, not from the current point.
Hence, paths will spiral outwards from the depot concentricly.
"""

def concentric(dim, distances, capacity, demand, findString):
    total = []
    solution = []
    while len(total) < dim - 1:
        distances, string = findString(distances, capacity, demand, False, True)
        s1 = string.copy()

        s1.remove(1)
        total.extend(s1)

        string.append(1)
        solution.append(string)
    return [solution, total]