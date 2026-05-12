def solution(num_list):

    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1

    return answer

# [짝수 개수, 홀수 개수] 를 반환
