def closestCoord(x_center, x1, x2):
    if (x_center < x1):
        x = x1
    elif (x_center > x2):
        x = x2
    else:
        x = x_center
    return x


def closestPoint(x_center, y_center, x1, y1, x2, y2):    
    x = closestCoord(x_center, x1, x2)
    y = closestCoord(y_center, y1, y2)    
    return x, y

def findDistance(x1, x2, y1, y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

def isOverlaped(x_center, y_center, radius, x, y):
    return findDistance(x_center, x, y_center, y) <= radius


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x,y = closestPoint(x_center, y_center, x1, y1, x2, y2)
        return isOverlaped(x_center, y_center, radius, x, y)
