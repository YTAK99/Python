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

  ###################################################################################################################
