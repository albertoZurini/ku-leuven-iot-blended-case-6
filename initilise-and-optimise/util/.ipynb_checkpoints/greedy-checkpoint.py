import numpy as np

# from distance matrix arr, find the first greedy string constraining to the capacity
def findGreedyString(arr, cap, demands, reverse, concentric):
    
    # choose depot-outward (greedy) or inward (greedy-reverse) paths 
    max = 1000000
    if reverse:
        max = 0
    
    # current node starts with depot (0 when 0-indexed)
    v = 0
    string = []
    dim = arr.shape
    total_demand = 0

    # while constraint: we could saturate the matrix before filling the capacity
    while not np.array_equal(arr, (np.ones(dim) * max).astype(int)):

        # append current node to the string
        string.append(int(v + 1))

        # disable this node
        arr[:, v] = max

        if not concentric:
            
            # find closest neighbour to node v
            if not reverse:
                nextv = np.argmin(arr[v])
            else:
                nextv = np.argmax(arr[v])
                
        else:
            
            # find the closest remaining node to the depot
            if not reverse:
                nextv = np.argmin(arr[0])
            else:
                nextv = np.argmax(arr[0])
            
        # stop if this node would overflow capacity
        if total_demand + int(demands[nextv]) >= cap:
            break

        # update demand of this truck when demand fits
        total_demand += int(demands[nextv])

        # update current node
        v = nextv
    return [arr, string]

def greedy(dim, distances, capacity, demand, cost, reverse=False):
    solution = []
    costs = []
    total = []
    arr = distances.copy()
    dist_og = distances.copy()
    
    while len(total) < dim - 1: # equals to: not np.array_equal(distances,(np.ones((dim,dim))*100000).astype(int)):
        
        # find next greedy string
        arr, string = findGreedyString(arr, capacity, demand, reverse, False)
        
        s1 = string.copy()
        s1.remove(1)
        total.extend(s1)

        string.append(1)
        solution.append(string)
        
        dist = cost(dist_og,string)
        costs.append(dist)
    return solution