class 클래스명:            # a.k.a. 붕어빵 틀과 붕어빵들
  정의



class BlackBox:
  pass
b1 = BlackBox()     # b1 객체 생성 완료
b1.name = '까망이'   # 변수 선언
print(b1.name)
print(isinstance(b1, BlackBox))     # True


# class: '붕어빵 틀'을 만드는 설계도

# BlackBox: 클래스의 이름 (보통 첫 글자를 대문자로)

# pass: 당장은 아무런 기능(메서드)이나 데이터(변수)를 넣지 않겠다는 빈 껍데기 선언

# b1: 설계도(BlackBox)를 바탕으로 실제로 만들어진 객체(Object)
# 붕어빵 틀에서 구워져 나온 '실제 붕어빵' 하나가 바로 b1

# 클래스 설계도에 미리 name이라는 변수를 만들어두지 않았더라도, 실행 중에 점(.)을 찍고 새로운 변수를 즉석에서 추가할 수 있다.

# b1.name = '까망이' : 이제 b1이라는 객체는 자신만의 name이라는 정보를 가지게 됨

# isinstance(b1, BlackBox) : "이 물건(b1)이 이 틀(BlackBox)에서 나온 게 맞니?" 라고 묻는 확인 도구


########################################################################################################################


class BlackBox:
    def __init__(self, name, price):        
        self.name = name
        self.price = price


# __init__ : 객체가 생성될 때 자동으로 호출되는 함수
# self : "나 자신". 붕어빵 틀에서 나온 '특정한 붕어빵' 그 자체
# name, price : 객체를 만들 때 외부에서 넣어줄 데이터들
# self. name : 멤버 변수

b1 = BlackBox('까망이', 200000)
print(b1.name, b1.price)
b2 = BlackBox('하양이', 100000)     # 똑같은 설계도로 만들었지만, b1과는 별개의 독립적인 객체
print(b2.name, b2.price)


########################################################################################################################


class BlackBox:
    def __init__(self, name, price):        
        self.name = name
        self.price = price

    def set_travel_mode(self):
        print('여행 모드 ON')

b1 = BlackBox('까망이', 200000)
b1.set_travel_mode()            # 실행 결과 : 여행 모드 ON





class BlackBox:
    def __init__(self, name, price):        
        self.name = name
        self.price = price


    def set_travel_mode(self, min): # 여행 모드 시간 (분)
        print(str(min) + '분 동안 여행 모드 ON')
    b1 = BlackBox('까망이', 200000)
    b1.set_travel_mode(20)          # 실행 결과 : 20분 동안 여행 모드 ON














