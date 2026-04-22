N = int(input())


for x in range(N, 0, -1):
    print(' ' * (N - x) + '*' * x)


for y in range(N, 0, -1):
    print(('*'*y).rjust(N))

# for z in range(N, 0, -1):
#     print("{:>5}".format('*' * z))
