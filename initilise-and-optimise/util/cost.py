# calculate total distance (cost) of a string
def cost(arr, string):
    distance = 0
    for i in range(len(string)-1):
        distance += int(arr[string[i]-1][string[i+1]-1])
    return distance