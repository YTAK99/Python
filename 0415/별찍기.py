i = 1

N = int(input())

while i <= N:
    print("*" * i)
    i += 1

#################################################################

N = int(input())
for i in range(N):
    for j in range(N):
        if i>=j:
            print("*", end='')
    print()