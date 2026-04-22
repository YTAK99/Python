N = int(input())

for y in range(5,0,-1):
        print('*'*y)

for x in range(N):
    for y in range(0, N-x):
        print('*', end='')
    print()
