''' 구구단 '''
dan = int(input("몇 단을 출력할까요? : "))

for i in range(1, 10):
    print("%d x %d = %2d" %(dan, i, dan * i))

########################################################################

''' 2중 for문 '''
for i in range(10):     # 열
    for j in range(3):  # 행
        print(f'[{i}, {j}]', end=' ')
    print()          # 한 단이 끝나면 줄바꿈

########################################################################

''' 구구단 - 2중 for문 '''
for i in range(1,10):
    for j in range(5,8):
        print(f'{j} * {i} = {j*i}', end='   ')
    print()

''' 구구단 - 2중 for문 행렬 차이점 '''
for i in range(5, 8):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}', end='   ')
    print()

##########################################################################

''' 입력받은 단으로 구구단 출력 (2 ≤ S,E ≤ 9) '''
s = int(input())    # 시작 단
e = int(input())    # 끝 단

# S가 E보다 큰 경우(예: 5단부터 3단까지)를 위해 step을 설정
step = 1 if s <= e else -1

for i in range(1, 10):    # 각 단마다 1부터 9까지 곱셉을 수행
    for dan in range(s, e + step, step):
        print(f"{dan} * {i} = {dan * i}", end="   ")
    
    print()     # 한 단이 끝나면 줄바꿈

