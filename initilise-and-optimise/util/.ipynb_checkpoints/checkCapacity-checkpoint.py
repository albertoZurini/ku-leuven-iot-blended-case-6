def checkCapacity(actual_cap, demands, string):
    cap = 0
    for i in range(1, len(string)-1):
        cap += int(demands[string[i]-1])
    if cap > actual_cap:
        #print('string ' + str(string) + ' has a capacity of ' + str(cap) + ' which is larger than ' + str(actual_cap))
        return False
    else:
        return True