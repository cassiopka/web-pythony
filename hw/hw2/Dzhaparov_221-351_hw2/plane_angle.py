import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Point(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

    def abs(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

def plane_angle(a, b, c, d):
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    cos_phi = x.dot(y) / (x.abs() * y.abs())
    phi = math.degrees(math.acos(max(min(cos_phi, 1), -1)))
    return phi

if __name__ == '__main__':
    a = Point(1, 1, 1)
    b = Point(2, 3, 4)
    c = Point(3, 2, 1)
    d = Point(4, 5, 6)
    angle = plane_angle(a, b, c, d)
    print(angle)
