# 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단

inp = input()

if inp == inp[::-1]:
    print(inp)
    print("입력하신 단어는 회문(Palindrome)입니다.")
