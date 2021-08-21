from random import random
import numpy as np
import random


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def __init__(self,s,e):
        self.x1=s[0]
        self.y1=s[1]
        self.x2=e[0]
        self.y2=e[1]
        self.sp=s
        self.ep=e


def getSlopeIntercept(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1) if x2-x1!=0 else 0
    c=y1-m*x1
    return (m,-c)


       
def getDualLine(points,l=-20,h=20,d=41):
    lines=[]
    lx = np.linspace(l,h,d)
    for p in points:
        ly = p.x*lx-p.y
        lines.append(Line((lx[0],ly[0]),(lx[-1],ly[-1])))
    return lines

def getDualPoint(lines):
    dualpoints=[getSlopeIntercept(l.x1,l.y1,l.x2,l.y2) for l in lines]
    return dualpoints

if __name__=='__main__':
    points=[Point(random.randint(-10,10),random.randint(-10,10)) for _ in range(10)]
    [print((p.x,p.y),end=',') for p in points]