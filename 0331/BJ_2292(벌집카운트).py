# 2292

# 1~1 -> 1        0
# 2~7 -> 2        5
# 8~19 -> 3       11
# 20~37 -> 4      17
# 38~61 -> 5      23
# 62~91 -> 6      29


N = int(input())

count = 1   # 지나가는 방 개수
end = 1     # 현재 범위의 마지막 번호

while N > end:
    end += 6 * count
    count += 1

print(count)
