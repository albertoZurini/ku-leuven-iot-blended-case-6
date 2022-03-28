def checkCapacity(actual_cap, demands, string):
    cap = 0
    for i in range(1, len(string)-1):
        cap += int(demands[string[i]-1])
    if cap > actual_cap:
        return False
    else:
        return True
    
def checkTotal(solutions, dim):
    total = []
    for string in solutions:
        copystring = string.copy()
        copystring.remove(1)
        copystring.remove(1)
        total.extend(copystring)
    if len(list(dict(zip(total,total)).keys())) < dim-1:
        return False
    return True

def checkSame(strings1, strings2):
    total1 = []
    for string in strings1:
        copystring = string.copy()
        copystring.remove(1)
        copystring.remove(1)
        total1.extend(copystring)
    
    total2 = []
    for string in strings1:
        copystring = string.copy()
        copystring.remove(1)
        copystring.remove(1)
        total2.extend(copystring)
    
    total1.sort()
    total2.sort()
    
    if total1 != total2:
        return False
    return True
        