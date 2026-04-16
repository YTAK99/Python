# 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산

# a = input()
# total = 0

# for x in range(1, 5):
#     total += int(a * x)

# print(total)



########################################################################


N = input()

sum = 0
str = N

for i in range(4):
    sum += int(str)
    str += N

print(sum)