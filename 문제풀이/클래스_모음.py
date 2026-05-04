#건물의 개수 N을 입력받고, 
# N개 건물의 건축연도와 가격을 입력받은 후, 
# 마지막 줄에 두 개의 정수 Y와 P를 입력받아 
# 건축연도가 Y년 이상이면서 가격이 P원 이하인 건물들을 
# 입력받은 순서대로 모두 출력하는 프로그램


class Building:
    def __init__(self, year, price):
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.price}"


N = int(input())
buildings = []

for _ in range(N):
    x, y = map(int, input().split())
    buildings.append(Building(x, y))

Y, P = map(int, input().split())

for b in buildings:
    if b.year >= Y and b.price <= P:
        print(b)

#### 출력 ####
#  Alex 11
#  Brown 56
# Alex(11) : child
# Brown(56) : adult


####################################################################################################################

#좌표 중심

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    def center(self, other):
        return Coordinate((self.x + other.x) / 2, (self.y + other.y) / 2)
    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

p1 = Coordinate(x1, y1)
p2 = Coordinate(x2, y2)

print("add =", p1 + p2)
print("sub =", p1 - p2)
print("center =", p1.center(p2))

###### 출력 ######
#  10.0 36.2
#  12.6 5.0
# add = 22.6, 41.2
# sub = -2.6, 31.2
# center = 11.3, 20.6


####################################################################################################################











