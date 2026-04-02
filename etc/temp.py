# class 클래스명:            # a.k.a. 붕어빵 틀과 붕어빵들
#   정의



# class BlackBox:
#   pass
# b1 = BlackBox()     # b1 객체 생성 완료
# b1.name = '까망이'   # 변수 선언
# print(b1.name)
# print(isinstance(b1, BlackBox))     # True


# class: '붕어빵 틀'을 만드는 설계도

# BlackBox: 클래스의 이름 (보통 첫 글자를 대문자로)

# pass: 당장은 아무런 기능(메서드)이나 데이터(변수)를 넣지 않겠다는 빈 껍데기 선언

# b1: 설계도(BlackBox)를 바탕으로 실제로 만들어진 객체(Object)
# 붕어빵 틀에서 구워져 나온 '실제 붕어빵' 하나가 바로 b1

# 클래스 설계도에 미리 name이라는 변수를 만들어두지 않았더라도, 실행 중에 점(.)을 찍고 새로운 변수를 즉석에서 추가할 수 있다.

# b1.name = '까망이' : 이제 b1이라는 객체는 자신만의 name이라는 정보를 가지게 됨

# isinstance(b1, BlackBox) : "이 물건(b1)이 이 틀(BlackBox)에서 나온 게 맞니?" 라고 묻는 확인 도구


########################################################################################################################

'''
나와 친구 두 사람의 키와 몸무게를 입력받아 각각의 내용을 출력
두 사람의 키와 몸무게의 합, 차의 절대값, 그리고 평균을 각각 구하여 출력

my 키: 150, 몸무게: 35.0
friend 키: 145, 몸무게: 41.2
plus 키: 295, 몸무게: 76.2
minus 키: 5, 몸무게: 6.2
avg 키: 147, 몸무게: 38.1
'''

class Person():
    def __init__(self, height, weight):
        self.height = int(height)
        self.weight = float(weight)

    def info(self):
        print(f"my 키: {self.height}, 몸무게: {self.weight}")
        return
    def your_info(self):
        print(f"friend 키: {self.height}, 몸무게: {self.weight}")
        return
    def add():
        print(f"{self.height+self.height}, 몸무게: {weight+weight}")
        return
    def sub():
        print(f"minus 키: {abs(height-height2)}, 몸무게: {abs(weight-weight2)}")
        return
    def avg():
        print(f"avg 키: {(height+height2)/2}, 몸무게: {(weight+weight2)/2}")
        return




    



height, weight = input('당신의 키와 몸무게를 입력하세요.').split()
I = Person(self)
I.append(Person(height, weight))

height2, weight2 = input('친구의 키와 몸무게를 입력하세요.').split()
YOU.append(Person(height2, weight2))

I.info(height, weight)




list???









































