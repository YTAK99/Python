'''
nums = [int(input()) for _ in range(7)]

odd = 0
oddlst = []

for n in nums:
    if (n % 2) != 0:
        odd += n
        oddlst.append(n)

if oddlst == []:
    print(-1)

else:
    print(odd)
    print(min(oddlst))
'''

## 최소값 직접 구하기 ##
nums = [int(input()) for _ in range(7)]

odd_sum = 0
min_val = 101       # 주어진 자연수가 100보다 작음
found = False       # 리스트를 안쓰는 대신 홀수가 존재하는지 기억

for n in nums:
    if n % 2 != 0:
        odd_sum += n
        found = True
        if n < min_val:     # 첫 값을 최소값으로 설정해놓고
            min_val = n     # 리스트를 돌면서 더 작은 값 나오면 갱신

if not found:       # True  (if min_val == 101 이렇게 해도됨)
    print(-1)       # 홀수 존재하지 않으면 -1 출력 
else:
    print(odd_sum)
    print(min_val)      # 최소값