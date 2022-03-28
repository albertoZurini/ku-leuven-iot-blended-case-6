import math

# calculate euclidean distance between two points: a (ax,ay) & b (bx,by)
def euc(a, b):
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )