변수 적을수록 좋다 = 공간 덜쓰니까

import keyword      # 예약어
print(keyword.kwlist)



type()    #데이터형 확인


bin()    # 정수형 데이터를 이진수로


ord()    # 실제 처리되는 값


x , y = 3, 5
answer = x > y
print(type(answer))   # <class 'bool'>
print(answer)       # False


x += 5    #x=x+5    # x의 값이 5증가
x *= 5    #x=x*5    # x는 5배수 값으로 변경


format(123456789, ',')  # 세자리마다 , 넣기




                  조건 반복              횟수 반복         무한 반복
--------------------------------------------------------------------
반복 기준   |      조건의 충족             반복 횟수         무한 실행
사용 예     |   지칠 때까지 반복하라      10번 반복하라       계속하라
반복문      |        while                  for           while True



































