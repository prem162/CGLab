import random
import numpy as np
import matplotlib.pyplot as plt

def get_cross_product(p1,p2,p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))

def get_slope(p1, p2):
    if p1[0] == p2[0]:
        return float('inf')
    else:
        return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])

def getDualLine(p,l=-20,h=20,d=41):
    lx = np.linspace(l,h,d)
    ly = p[0]*lx-p[1]
    return [lx[0],lx[-1]],[ly[0],ly[-1]]

def getSlopeIntercept(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1) if x2-x1!=0 else 0
    c=y1-m*x1
    return (m,-c)

def computeHull(points):    
    hull=[]
    points.sort(key=lambda x:[x[0],x[1]])
    start = points.pop(0)
    hull.append(start)
    points.sort(key=lambda p: (get_slope(p,start), -p[1],p[0]))
    for pt in points:
        hull.append(pt)
        while len(hull) > 2 and get_cross_product(hull[-3],hull[-2],hull[-1]) < 0:
            hull.pop(-2)
    hull.append(hull[0])
    return hull
def computeUpperHull(points):
    rPoint=max(points)
    lPoint=min(points)
    uHull=[]
    uHull.append(rPoint)
    points.sort(key=lambda p: (get_slope(p,rPoint), -p[1],p[0]))
    for pt in points:
        uHull.append(pt)
        while len(uHull) > 2 and get_cross_product(uHull[-3],uHull[-2],uHull[-1]) < 0:
            uHull.pop(-2)
        if pt==lPoint:
            break
        
    return uHull


if __name__=='__main__':
    n=int(input('No of points : '))
    _=input('Range of values(give space between two intervals): ')
    a,b=[int(n) for n in _.split()]
    print('{n} random points generates in interval [{a},{b}].')
    points=[(random.randint(a,b), random.randint(a,b)) for _ in range(n)]
    print('appling Grahams scan algorithm.....')
    hull=computeHull(points.copy())
    print('Hull points : ',hull)
    print('Computing upper hull....')
    uHull=computeUpperHull(hull.copy())
    print('Upper hull points : ',uHull)
    lHull=[p  for p in hull if p not in uHull]
    print('Lower Hull points :',lHull)
    print('Total no. of envelop in Dual plane is: ',len(uHull)+len(lHull))
    print('The Graphical Represantation is Showing......')
    plt.subplot(1,2,1)
    plt.title('Convex Hull')
    plt.plot([p[0] for p in points],[p[1] for p in points],marker='o',linestyle='none',color='b')
    #plt.plot([p[0] for p in hull],[p[1] for p in hull],color='')
    #plotLines(plt,hull)
    plt.plot([p[0] for p in uHull],[p[1] for p in uHull],color='y')
    plt.plot([p[0] for p in lHull],[p[1] for p in lHull],color='g')
    plt.legend()
    plt.subplot(1,2,2)
    plt.title('Dual Lines')
    for p in uHull:
        sx,sy=getDualLine(p)
        plt.plot(sx,sy,color='g')

    for p in lHull:
        sx,sy=getDualLine(p)
        plt.plot(sx,sy,color='y')   
    ldPoint=[]
    for i in range(len(uHull)-1):
        p1,p2=uHull[i],uHull[i+1]
        ldPoint.append(getSlopeIntercept(p1[0],p1[1],p2[0],p2[1]))
    plt.plot([p[0] for p in ldPoint],[p[1] for p in ldPoint],marker='o',linestyle='none',color='y')
    udPoint=[]
    for i in range(len(lHull)-1):
        p1,p2=lHull[i],lHull[i+1]
        udPoint.append(getSlopeIntercept(p1[0],p1[1],p2[0],p2[1]))
    plt.plot([p[0] for p in udPoint],[p[1] for p in udPoint],marker='d',linestyle='none',color='g')
    plt.show()
    print('Process completed.')