# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
# 길이가 0보다 크고 80보다 작은 문자열이 주어진다.





N = int(input())

for x in range(N):
    total_sum = 0   # 총 합계
    current_score = 0   # 현재 연속된 O 점수 (a.k.a.가산점)

    ox = input()
    
    for i in ox:
        if i == 'O':
            current_score += 1
            total_sum += current_score
        elif i == 'X':
            current_score = 0

    # print(ox)
    print(total_sum)