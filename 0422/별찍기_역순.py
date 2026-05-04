N = int(input())

for y in range(5,0,-1):
        print('*'*y)

for x in range(N):
    for y in range(0, N-x):
        print('*', end='')
    print()

########################################################################################

# 자리 맞춰서 출력

N = int(input())

for x in range(N):
    for y in range(x):
        print(" ", end="")
        
    for z in range(N-x, 0, -1):
        print("*", end="")
    print()
