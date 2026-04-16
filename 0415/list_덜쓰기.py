# A2 = []
# A3 = []

# N = int(input())
# for x in range(N):
#     nums = int(input())

#     if nums % 2 == 0:
#         A2.append(nums)
#     if nums % 3 == 0:
#         A3.append(nums)

# print(f"2의 배수:", len(A2))
# print(f"3의 배수:", len(A3))

###############################################################

count2 = 0
count3 = 0

N = int(input())

for _ in range(N):
    nums = int(input())

    if nums % 2 == 0:
        count2 += 1
    if nums % 3 == 0:
        count3 += 1

print("2의 배수:", count2)
print("3의 배수:", count3)

'''
리스트 안 써도 되는 경우

개수만 필요할 때 (지금처럼 👍)
합, 평균 같은 누적값만 필요할 때
'''