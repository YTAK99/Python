사각형의 높이 n과 너비 m을 입력받은 후, 사각형 내부에 지그재그 형태로 1부터 n*m번까지 숫자가 차례대로 출력되는 프로그램

############################################################################################################################################################

n, m = map(int, input().split())

for i in range(n):
    start = i * m + 1

    if i % 2 == 0:
        for j in range(start, start + m):
            print(j, end=" ")
    else:
        for j in range(start + m - 1, start - 1, -1):
            print(j, end=" ")

    print()

############################################################################################################################################################

n, m = map(int, input().split())

for i in range(n):
    start = i * m + 1

    if i % 2 == 0:
        # 왼 -> 오른쪽
        for j in range(start, start + m):
            print(j, end=" ")
    else:
        # 오른 -> 왼쪽
        for j in range(start + m - 1, start - 1, -1):
            print(j, end=" ")

    print()

############################################################################################################################################################

n, m = map(int, input().split())

num = 1

for i in range(n):
    row = []

    # 한 줄 채우기
    for j in range(m):
        row.append(num)
        num += 1

    # 방향 바꾸기
    if i % 2 == 1:
        row.reverse()

    # 출력
    for x in row:
        print(x, end=" ")
    print()
