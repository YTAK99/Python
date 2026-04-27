class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    def __truediv__(self, value):
        return Coordinate(self.x / value, self.y / value)
   
    # def center(self, other):
    #     return Coordinate((self.x + other.x) / 2, (self.y + other.y) / 2)
    # # def center(p1, p2):
    # return Coordinate((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    
    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

p1 = Coordinate(x1, y1)
p2 = Coordinate(x2, y2)

print("add =", p1 + p2)
print("sub =", p1 - p2)
# print("center =", p1.center(p2))

center = (p1 + p2) / 2
print("center =", center)
