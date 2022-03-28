import numpy as np

def getDist(dim, x, y, dist_calc, maximize=True):
    filler = 0
    if maximize:
        filler = 1000000
    distances = np.zeros((dim,dim))
    for v in range(dim):
        for u in range(dim):
            distances[v][u] = round(
                dist_calc(
                    (int(x[u]), int(y[u])),
                    (int(x[v]), int(y[v]))
                )
            )
            if u==v:
                distances[v][u] = filler
    return distances.astype(int)
    