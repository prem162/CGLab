from collections import namedtuple  
import matplotlib.pyplot as plt  
import random
import numpy as np
from plot import *
Point = namedtuple('Point', 'x y')


class ConvexHull(object):  
    _points = []
    _hull_points = []

    def __init__(self):
        pass

    def add(self, point):
        self._points.append(point)

    def _get_orientation(self, origin, p1, p2):
        '''
        Returns the orientation of the Point p1 with regards to Point p2 using origin.
        Negative if p1 is clockwise of p2.
        :param p1:
        :param p2:
        :return: integer
        '''
        difference = (
            ((p2.x - origin.x) * (p1.y - origin.y))
            - ((p1.x - origin.x) * (p2.y - origin.y))
        )

        return difference

    def compute_hull(self):
        '''
        Computes the points that make up the convex hull.
        :return:
        '''
        points = self._points

        # get leftmost point
        start = points[0]
        min_x = start.x
        for p in points[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        #print('start',start)
        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            # get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # ensure we aren't comparing to self or pivot point
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    #print(p1,p2,direction)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def slopeIntercept(self,x1,y1,x2,y2):
        dx=x2-x1 if x1<x2 else x1-x2
        dy=y2-y1 if y1<y2 else y1-y2
        m=dy/dx if dx!=0 else 0
        c=y1-m*x1
        return (m,-c)

    def display(self):
        plt.subplot(1,2,1)
        # all points
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker='D', linestyle='None')

        # hull points
        print('no of points',len(self._hull_points))
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy)
        plt.plot(hx[-1],hy[-1],marker='d')
        plt.title('Convex Hull')
    
    def displayDual(self):
        plt.subplot(1,2,2)
        # hull points
        hx = [p.x for p in self._hull_points[1:]]
        hy = [p.y for p in self._hull_points[1:]]
        x1=[ls[0] for ls in self._hull_points[:len(self._hull_points)]]
        y1=[ls[1] for ls in self._hull_points[:len(self._hull_points)]]
        x2=[ls[0] for ls in self._hull_points[1:]]
        y2=[ls[1] for ls in self._hull_points[1:]]
        points=[self.slopeIntercept(x1[i],y1[i],x2[i],y2[i]) for i in range(len(x1)-1)]
        x=[p[0] for p in points]
        y=[p[1] for p in points]
        print('len of intersect',len(x))
        for i in range(len(hx)):
            lx = np.linspace(-10,10,50)
            ly = hx[i]*lx-hy[i]
            plt.plot(lx, ly, '-r')
        plt.title('Dual Line')
        plt.plot(x,y,marker='o',color='b',linestyle='none')
        plt.show()
    
    




def main():  
    ch = ConvexHull()
    for _ in range(20):
        ch.add(Point(random.randint(-100, 100), random.randint(-100, 100)))
    #ch._points=[Point(p[0],p[1]) for p in defaultPoints]
    print("Points on hull:", ch.get_hull_points())
    #ch.display()
    #ch.displayDual()
    plt.subplot(1,2,1)
    plt.title('Convex Hull')
    plotPoints(plt,ch._points)
    plotLines(plt,ch._hull_points)
    plt.subplot(1,2,2)
    plt.title('Dual Line')
    plotDualLine(plt,ch._hull_points)
    plt.show()

if __name__ == '__main__':  
    main()