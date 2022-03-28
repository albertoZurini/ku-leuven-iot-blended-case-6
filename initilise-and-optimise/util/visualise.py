import matplotlib.pyplot as plt

def visCost(costs, type):
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.scatter(list(range(1,len(costs)+1)), costs, s=50, facecolor='C0', edgecolor='k');
    plt.xlabel('string found')
    plt.ylabel('cost')
    plt.title(type)
    
def visCostCum(costs, type):
    cumsum = [sum(costs[0:i]) for i in range(len(costs))]
    plt.plot(cumsum)
    plt.xlabel('string found')
    plt.ylabel('cumulative cost')
    plt.title(type)
    plt.show()
    
def paths(x, y, strings, type, opt, depot=True):
    solutions = strings
    if not depot:
        solutions = strings.copy()
        [sol.remove(1) for sol in solutions]
        [sol.remove(1) for sol in solutions]
    plt.figure(figsize=(4, 4), dpi=80)
    plt.scatter([int(xi) for xi in x], [int(yi) for yi in y], s=10, facecolor='white', edgecolor='k')
    plt.scatter(int(x[0]), int(y[0]), s=50, facecolor='k', edgecolor='k')
    if opt:
        plt.title(type + ' - optimized')
    else:
        plt.title(type + ' - initial')

    for string in solutions:
        xs = [int(x[xi-1]) for xi in string]
        ys = [int(y[yi-1]) for yi in string]
        plt.plot(xs,ys)