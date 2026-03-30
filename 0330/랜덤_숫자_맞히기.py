import random        # random 모듈 불러오기
answer = random.randint(1, 20)    # 1에서 20 사이의 랜덤 정수 저장

number = 0

while number != answer:
  number = int(input("숫자 입력(1~20) : "))

  if number > answer:
    print("↓")
  elif number < answer:
    print("↑")
  else:
    print("★정답★")
