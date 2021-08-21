from random import randint
from math import sqrt
import pygame

wid, hei = 1000,600 #window width and height

def generateRandomPoints(n): #generate random points
    return sorted([[randint(10,wid-10),randint(10,hei-10)] for f in range(0,n)])
def generateGrid(n): #generate non-random points
    points=[]
    for i in range(0,int(sqrt(n))):
        for j in range(0,int(sqrt(n))):
            points.append([i*wid/int(sqrt(n))+50*(i%2==0 and j%2==0),j*hei/int(sqrt(n))])
    return sorted(points)
def determinant(points):
    #takes input [[x1,y1],[x2,y2]],[x3,y3]
    """determinant of 3x3 matrix:
    points[0].x, points[0].y, 1
    points[1].x, points[1].y, 1
    cand.x,      cand.y,      1
    """
    #partial upper is only ever a list of 2
    #cand = [x,y] (candidate point that is next after points[1]
    return (points[1][0]-points[0][0])*(points[2][1]-points[0][1])-(points[1][1]-points[0][1])*(points[2][0]-points[0][0])

class viewPoints():
    def __init__(self,points):
        self.animate=0
        self.width=wid
        self.height=hei
        self.points=points
        self.hullPoints=[]
        self.screen = pygame.display.set_mode([self.width,self.height])
        self.colors=[(255,0,0),(0,255,0),(0,0,255)]
    def toggleAnimate(self): #turn on or off animations
        self.animate = not self.animate
    def drawPoints(self):
        self.screen.fill((0,0,0)) #fill screen
        for i1,point in enumerate(self.points): #draw each point
            pygame.draw.circle(self.screen, self.colors[i1%3], [point[0],point[1]], 2, 1)
        pygame.display.update()
    def debugDrawHull(self): #highlights points after the scan is complete
        self.drawPoints()
        for j in range(0,len(self.hullPoints)-1):
            print("%s: %s, %s" %(j,self.hullPoints[j][0],self.hullPoints[j][1]))
            pygame.draw.line(self.screen,
                                 (0,255,0),
                                 [self.hullPoints[j][0],self.hullPoints[j][1]],
                                 [self.hullPoints[j+1][0],self.hullPoints[j+1][1]],
                                 1)
            pygame.draw.circle(self.screen, (255,255,0), [self.hullPoints[j+1][0],self.hullPoints[j+1][1]], 20, 1)
        pygame.draw.line(self.screen,
                                 (0,255,0),
                                 [self.hullPoints[-1][0],self.hullPoints[-1][1]],
                                 [self.hullPoints[0][0],self.hullPoints[0][1]],
                                 1)
        pygame.display.update()
        pygame.time.delay(100)

    def scan(self):
        #start upper scan
        upper=self.points[:2]
        for i in range(2,len(self.points)):
            upper.append(self.points[i])
            while len(upper) > 2 and determinant([upper[-3],upper[-2],upper[-1]]) < 0:
                del upper[-2]
                if self.animate==1: #animate
                    self.drawPoints()
                    for j,point in enumerate(upper[:-1]):
                        pygame.draw.line(self.screen,
                                             (255,255,255),
                                             [upper[j][0],upper[j][1]],
                                             [upper[j+1][0],upper[j+1][1]],
                                             1)
                        pygame.display.update()
                    pygame.time.delay(20)

        #start lower scan
        lower=[upper[-1],self.points[-1]]
        for i in range(len(self.points)-2,-1,-1):
            lower.append(self.points[i])
            while len(lower) > 2 and determinant([lower[-3],lower[-2],lower[-1]]) < 0:
                del lower[-2]
                if self.animate==1: #animate
                    self.drawPoints()
                    for j,point in enumerate(upper[:-1]):
                        pygame.draw.line(self.screen,
                                             (255,255,255),
                                             [upper[j][0],upper[j][1]],
                                             [upper[j+1][0],upper[j+1][1]],
                                             1)
                    for j,point in enumerate(lower[:-1]):
                        pygame.draw.line(self.screen,
                                             (255,255,255),
                                             [lower[j][0],lower[j][1]],
                                             [lower[j+1][0],lower[j+1][1]],
                                             1)
                        pygame.display.update()
                    pygame.time.delay(20)

        self.hullPoints = [f for n,f in enumerate(upper+lower) if f not in [upper+lower][:n]]
        for j in range(0,len(self.hullPoints)-3):
            pygame.draw.line(self.screen,
                                     (255,255,255),
                                     [self.hullPoints[j][0],self.hullPoints[j][1]],
                                     [self.hullPoints[j+1][0],self.hullPoints[j+1][1]],
                                     1)
        self.debugDrawHull()

    def start(self):
        pygame.init()
        self.screen.fill((0,0,0))
        for i1,point in enumerate(self.points):
            pygame.draw.circle(self.screen, self.colors[i1%3], [point[0],point[1]], 2, 1) #draw each point with the next color in the list
        self.scan()

if __name__=="__main__":
    #for i in range(0,10): #run a few times
        obj1 = viewPoints(generateRandomPoints(50)) #scan random points
        obj2 = viewPoints(generateGrid(randint(10,50))) #scan non-random points
        obj1.toggleAnimate() #turns animations on/off
        obj1.start()
        pygame.display.update() #update newly drawn points and lines
        pygame.quit()