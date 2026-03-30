message = '전역 변수임다'

print(message)      # '전역 변수임다' 출력


def no_secret():
    message = '지역 변수임다'    # 지역 변수임
    print(message)
no_secret()         # '지역 변수임다' 출력


def no_secret2():
    global message
    print(message)
no_secret2()        # '전역 변수임다' 출력


def no_secret3():
    global message
    message = '전역 변수 값 변경'
    print(message)
no_secret3()        # '전역 변수임다' 출력
print(message)















