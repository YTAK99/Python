# 어디어디 숨었나
# ㅁ   ㅁ   ㅁ   ㅁ   ㅁ   ㅁ   ㅁ
# [0]  [1]  [2]  [3]  [4]  [5]  [6]
#  2    4    8    16   4    1    4

# N개의 상자
N = int(input())   # ex) 7개
box = []

# 박스에 번호 붙이기
for _ in range(1, N+1):   # A1부터 AN까지
    A = int(input())   # ex) 2 4 8 16 4 1 4
    box.append(A)

# 숫자 K가 적힌 상자 (후에 개수 찾아야함(출력))
K = int(input())    # ex) 4

# 출력 2 5 7

for i in range(len(box)):
    if box[i] == K:
        print(i+1, end=' ')   # 문제에서 1번부터 시작하니까 +1