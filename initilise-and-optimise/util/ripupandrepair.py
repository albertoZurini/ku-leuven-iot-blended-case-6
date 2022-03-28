def findOpt(string, ogstring, pool, arr, cost, force):

    # only half of points need to be used if there is another string to be filled
    metric = round(len(pool)/2)
    if force:
        metric = 0
    
    bestsolution = string.copy()
    thesenodes = pool.copy()
    while len(thesenodes) > metric:
        
        # force any point in the shortened string by artficially rasiing its cost
        costtobeat = 1000000
        
        # keep track of which node has been tried where
        used = None
        place = 0
        
        # try all nodes in all positions of a copy of the best solution
        for node in thesenodes:
            for i in range(1,len(bestsolution)):
                tempsol = bestsolution.copy()
                tempsol.insert(i, node)
                tempcost = cost(arr, tempsol)
                if tempcost < costtobeat:
                    
                    # cache this 'more optimal' solution
                    used = node
                    place = i
                    costtobeat = tempcost
        
        # insert cached solution
        bestsolution.insert(place,used)
        thesenodes.remove(used)
        
    return [bestsolution, costtobeat, thesenodes]