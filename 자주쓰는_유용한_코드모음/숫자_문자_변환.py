def solution(age):
    alpha = "abcdefghij"
    answer = ""

    for i in str(age):
        answer += alpha[int(i)]

    return answer

print(solution(23))
print(solution(100))
