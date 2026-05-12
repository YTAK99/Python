def solution(age):
    alpha = "abcdefghij"
    answer = ""

    for i in str(age):
        answer += alpha[int(i)]        # 문자열도 인덱싱 가능

    return answer

print(solution(23))
print(solution(100))
