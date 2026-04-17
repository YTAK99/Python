col, row = map(int, input("[행 열]을 입력하세요: ").split())

for x in range(1, col+1):    # 행(가로선)
    for y in range(1, row+1):   # 열(세로선)
        print(f'({x}행 X {y}열)', end=' ')
    print()
    print()

########################################################################

cr = int(input("정방행렬 크기를 입력하세요: "))

for m in range(1, cr+1):    # 행 m
    for n in range(1, cr+1):   # 열 n
        print(f'({m}, {n})', end=' ')
    print()
    print()