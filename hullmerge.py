class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cw_next = None
        self.ccw_next = None

    def subtract(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

def merge(chull1, chull2):
    # get the rightmost point of left convex hull
    p = max(chull1, key = lambda point: point.x)

    # get the leftmost poitn of right convex hull
    q = min(chull2, key = lambda point: point.x)

    # make copies of p and q
    cp_p = p
    cp_q = q

    # raise the bridge pq to the uper tangent
    prev_p = None
    prev_q = None
    while (True):
        prev_p = p
        prev_q = q
        if q.cw_next:
            # move p clockwise as long as it makes left turn
            while direction(p, q, q.cw_next) < 0:
                q = q.cw_next
        if p.ccw_next:
            # move p as long as it makes right turn
            while direction(q, p, p.ccw_next) > 0:
                p = p.ccw_next

        if p == prev_p and q == prev_q:
            break
    
    # lower the bridge cp_p cp_q to the lower tangent
    prev_p = None
    prev_q = None
    while (True):
        prev_p = cp_p
        prev_q = cp_q
        if cp_q.ccw_next:
            # move q as long as it makes right turn
            while direction(cp_p, cp_q, cp_q.ccw_next) > 0:
                cp_q = cp_q.ccw_next
        if cp_p.cw_next:
            # move p as long as it makes left turn
            while direction(cp_q, cp_p, cp_p.cw_next) < 0:
                cp_p = cp_p.cw_next
        if cp_p == prev_p and cp_q == prev_q:
            break

    # remove all other points
    p.cw_next = q
    q.ccw_next = p

    cp_p.ccw_next = cp_q
    cp_q.cw_next = cp_p

    # final result
    result = []
    start = p 
    while (True):
        result.append(p)
        p = p.ccw_next

        if p == start:
            break

    return result

if __name__ == '__main__':
    p1 = Point(2, 2)
    p2 = Point(3, 4)
    p3 = Point(7, 3)
    p4 = Point(5, 2)
    p5 = Point(7, 5)
    p6 = Point(5, 6)

    p1.cw_next = p2 
    p1.ccw_next = p4
    p2.cw_next = p6
    p2.ccw_next = p1
    p3.cw_next = p4
    p3.ccw_next = p5
    p4.cw_next = p1 
    p4.ccw_next = p3 
    p5.cw_next = p3
    p5.ccw_next = p6
    p6.cw_next = p5
    p6.ccw_next = p2

    p7 = Point(11, 5)
    p8 = Point(15, 7)
    p9 = Point(12, 3)
    p10 = Point(15, 3)
    p11 = Point(16, 5)
    p12 = Point(12, 7)

    p7.cw_next = p12
    p7.ccw_next = p9
    p8.cw_next = p11
    p8.ccw_next = p12
    p9.cw_next = p7
    p9.ccw_next = p10
    p10.cw_next = p9
    p10.ccw_next = p11
    p11.cw_next = p10
    p11.ccw_next = p8
    p12.cw_next = p8
    p12.ccw_next = p7

    p = merge([Point(1, 1)], [Point(0, 0)])
    print(p)