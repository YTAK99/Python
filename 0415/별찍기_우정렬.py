'''

''  *
4   1
3   2
2   3
1   4
0   5

'''

##################################################################

N = int(input())

for row in range(N):
    for col in range(N-row-1):
        print(" ", end='')
    for col2 in range(row+1):
        print("*", end='')
    print()

##################################################################

N = int(input())

for i in range(1, N + 1):
    # 1. 공백 출력 (N-i번 반복)
    for j in range(N - i):
        print(" ", end="")
    
    # 2. 별 출력 (i번 반복)
    for k in range(i):
        print("*", end="")
    
    # 3. 한 줄이 끝나면 줄바꿈
    print()

##################################################################

N = int(input())

for i in range(1, N + 1):
    blank = " " * (N - i)
    stars = "*" * i
    print(blank + stars)

##################################################################

N = int(input())
for i in range(1, N + 1):
    print(("*" * i).rjust(N))       # 오른쪽 정렬을 도와주는 메서드
# 전체 길이를 N으로 잡고 오른쪽으로 정렬한 뒤 남은 공간을 공백으로 채운다