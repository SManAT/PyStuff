"""
Basic 2D Vector Module
"""

import math


class Vector2D:
    x = 0
    y = 0

    # Konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[%s,%s]" % (self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
        
    def scalar(self, k):
        self.x *= k
        self.y *= k

def createVecFromPoints(A, B):
        """Create Vector from A > B"""
        x = B[0] - A[0]
        y = B[1] - A[1]
        return Vector2D(x,y)

if __name__ == "__main__":
    # Running some Tests
    a = Vector2D(12, 2)
    print(a)
    print("Length %s: %s" % (a, a.length()))

    P1 = [4, 5]
    P2 = [-3, 2]
    createVecFromPoints(P1, P2)
    print("P1 > P2: %s > %s = %s" % (P1, P2, a))
