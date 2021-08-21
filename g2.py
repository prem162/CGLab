import random
import matplotlib.pyplot as plt
from dual import *

def get_cross_product(p1,p2,p3):
    return ((p2.x - p1.x)*(p3.y - p1.y)) - ((p2.y - p1.y)*(p3.x- p1.x))

def get_slope(p1, p2):
    if p1.x == p2.x:
        return float('inf')
    else:
        return 1.0*(p1.y-p2.y)/(p1.x-p2.x)
def computeHull(points):    
    hull=[]
    points.sort(key=lambda p:[p.x,p.y])
    start = points.pop(0)
    hull.append(start)
    points.sort(key=lambda p: (get_slope(p,start), -p.y,p.x))
    for pt in points:
        hull.append(pt)
        while len(hull) > 2 and get_cross_product(hull[-3],hull[-2],hull[-1]) < 0:
            hull.pop(-2)
    
    return hull

def computeUpperHull(points):
    rPoint=max(points)
    lPoint=min(points)
    #return points[points.index(rPoint):points.index(lPoint)+1]
    uHull=[]
    uHull.append(rPoint)
    points.sort(key=lambda p: (get_slope(p,rPoint), -p.y,p.x))
    for pt in points:
        uHull.append(pt)
        if pt==lPoint:
            break
        while len(uHull) > 2 and get_cross_product(uHull[-3],uHull[-2],uHull[-1]) < 0:
            uHull.pop(-2)
        
    return uHull


if __name__=='__main__':
    points=[Point(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(50)]
    hull=computeHull(points.copy())
    [print((h.x,h.y),end=',') for h in hull]
    plt.subplot(1,2,1)
    plt.title('Convex Hull')
    plt.plot([p.x for p in points],[p.y for p in points],marker='o',linestyle='none')
    '''uHull=computeUpperHull(hull.copy())
    lHull=[p  for p in hull if p not in uHull]
    print(uHull)
    print(lHull)
    plt.plot([p[0] for p in uHull],[p[1] for p in uHull],label='UH')
    plt.plot([p[0] for p in lHull],[p[1] for p in lHull],Label='LH')
    plt.legend()'''
    plt.subplot(1,2,2)
    plt.title('Dual Lines')
    dLines=dualLine(hull)
    for l in dLines:
        plt.plot([l.x1,l.x2 ],[l.y1 ,l.y2] ,color='r' )
    plt.show()