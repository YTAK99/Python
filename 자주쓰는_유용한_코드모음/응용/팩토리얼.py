# 정수 n이 주어질 때 i! ≤ n 을 만족하는 
# 가장 큰 정수i 를 return

def solution(n):
    fact = 1
    i = 1

    while fact <= n:
        i += 1
        fact *= i

    return i - 1

print(solution(7))      # = 3
print(solution(3628800))    # = 10


##########################################################################
# import math
# def solution(n):
#     t=1
#     while n>=math.factorial(t):
#         t+=1
#     return t-1
