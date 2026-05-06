# N명, N개의 카드
# A [] vs B []
# 이긴 그룹에서 C [] vs D [] => (i+j)//2
# 각각 1명이 되면 비교해서 승자를 가림. -> 다시 더 큰 그룹 승자 뽑음
# 1:가위 2:바위 3:보  / 같은 카드면 번호가 작은쪽이 승자



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    def winner(a, b):
        if cards[a] == cards[b]:
            return a

        if (cards[a] == 1 and cards[b] == 3) or \
           (cards[a] == 2 and cards[b] == 1) or \
           (cards[a] == 3 and cards[b] == 2):
            return a
        else:
            return b

    def tournament(left, right):
        if left == right:
            return left

        mid = (left + right) // 2

        l = tournament(left, mid)
        r = tournament(mid + 1, right)

        return winner(l, r)

    result = tournament(0, N - 1)

    print(f"#{tc} {result + 1}")  # 사람 번호는 1부터
