# 예시
# CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
# CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
# CAA 연속 문자 AA를 지운다.
# C 1글자가 남았으므로 1을 리턴한다.


def remove_repeat(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:   # 스택이 비어있지 않고, 마지막 문자와 현재 문자가 같다면
            stack.pop()
        else:
            stack.append(ch)

    #print(stack)
    return len(stack)


T = int(input())

for tc in range(1, T + 1):
    s = input().strip()

    result = remove_repeat(s)

    print(f"#{tc} {result}")
