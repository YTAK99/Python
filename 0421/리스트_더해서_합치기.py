a, b = map(int, input().split())
c, d = map(int, input().split())

newlst = [*([a]*b), *([c]*d)]

print(newlst)