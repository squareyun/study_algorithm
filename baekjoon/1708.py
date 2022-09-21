#TITLE: 볼록 껍질 (https://www.acmicpc.net/problem/1708)
#LEVEL: P5
#TAG: convex_hull, geometry
#DATE: 20220921
#AUTHOR: squareyun

import math

def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0: return True
    else: return False

def grahamScan(points):
    convexHull = []
    pointsWithAngle = []
    
    # 최초 포함하는 점 p 찾기
    points.sort(key = lambda x: (x[1], -x[0])) # y값 가장 작은 점, x값 가장 큰 점
    p = points[0]
    convexHull.append(p)
    
    # 각도 계산
    for i in range(1, len(points)):
        px, py = p[0], p[1]
        ax, ay = points[i][0], points[i][1]
        angle = math.atan2(ay - py, ax - px)
        pointsWithAngle.append((ax, ay, angle))
    
    pointsWithAngle.sort(key = lambda x: x[2])
    
    for a in pointsWithAngle:
        convexHull.append((a[0], a[1]))

        while len(convexHull) >= 3:
            k = convexHull[-1]
            j = convexHull[-2]
            i = convexHull[-3]
            if ccw(i, j, k):
                break
            else:
                k = convexHull.pop()
                j = convexHull.pop()
                convexHull.append(k)

    return(len(convexHull))

n = int(input())
points = []
for i in range(n):
    a, b = map(int,input().split())
    points.append((a,b))
print(grahamScan(points))