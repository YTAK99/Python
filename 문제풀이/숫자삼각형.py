##################################################################################

# 기본 코드
n = int(input())

# 입력 조건 체크
if n < 1 or n > 50 or n % 2 == 0:
    print("INPUT ERROR!")
else:
    for i in range(n):
        start = i * (i + 1) // 2 + 1

        if i % 2 == 0:
            # 정방향
            for j in range(start, start + i + 1):
                print(j, end=" ")
        else:
            # 역방향
            for j in range(start + i, start - 1, -1):
                print(j, end=" ")

        print()


##################################################################################


# 리스트로 푼 코드
n = int(input())

# 입력 조건 체크
if not (1 <= n <= 50 and n % 2 != 0):
    print("INPUT ERROR!")
else:
    num = 1

    for i in range(n):
        row = []

        # i+1개 채우기
        for j in range(i + 1):
            row.append(num)
            num += 1

        # 방향 바꾸기
        if i % 2 == 1:
            row.reverse()

        print(*row)


##################################################################################


# 더 간단한 코드
n = int(input())

if n < 1 or n > 50 or n % 2 == 0:
    print("INPUT ERROR!")
else:
    num = 1

    for i in range(n):
        row = list(range(num, num + i + 1))
        num += i + 1

        if i % 2 == 1:
            row.reverse()

        print(*row)
