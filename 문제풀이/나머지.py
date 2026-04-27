# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

lst = []
newlst = []
count = 0

for _ in range(10):
    lst.append(int(input()))

for x in lst:
    newlst.append(x % 42)

for y in newlst:
    if y not in newlst[:count]:
        count += 1

print(count)

########################################################################

newlst = []
unique = []

for _ in range(10):
    num = int(input()) % 42
    newlst.append(num)

for x in newlst:
    if x not in unique:
        unique.append(x)

print(len(unique))

########################################################################

lst = []

for _ in range(10):
    lst.append(int(input()) % 42)

print(len(set(lst)))
