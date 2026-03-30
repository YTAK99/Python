dictionary = {key1:value1, key2:value2, ... }

예1) person = {“이름”: “나귀욤”, “나이”: 7,“키”: 120, “몸무게”: 23}

예2)
person = {
“이름”: “나귀욤”,
“나이”: 7,
“키”: 120,
“몸무게”: 23
}

print(person["이름"])   # 나귀욤 출력


person = {'이름': '나귀욤', 
    '나이': 7, 
    '키': 120, 
    '몸무게': 23}
print(person['나이'])    # 7 출력
print(person.get(“별명”))   # 없는 key 에 접근하면 None 출력


person['최종학력'] = '유치원'    # 새로운 데이터 추가
print(person)   # {'이름': '나귀욤', '나이': 7, '키': 120, '몸무게': 23, '최종학력': '유치원'}

person['키'] = 130      # 특정 key의 value를 바꾸려면
print(person)

person.update({'키': 130, '몸무게': 99})   # 여러 key들의 value 변경
print(person)

person.pop('몸무게')       # 특정 key:value를 삭제
print(person)

person.clear()      # 모든 데이터 삭제
print(person)

print(person.keys())        # 어떤 key 들이 있는지지

print(person.values())      # 어떤 value 들이 있는지

print(person.items())       # 어떤 key:value 들이 있는지

# fromkeys()    제공된 keys 를 통해 새로운 딕셔너리 생성 및 반환
# popitem()     마지막으로 추가된 데이터 삭제
# setdefault()      key에 해당하는 value 반환. key가 없다면 새로 만들고 default value 설정 및 반환


################################################################################################


my_tuple = ('오예스', '몽쉘')
my_list = list(my_tuple)        # list로 바꾸면 수정, 추가, 삭제 가능

################################################################################################

my_list = [1,2,3,4,5,5]
print(my_list)
my_set = set(my_list)
print(my_set)
my_list = list(my_set)
print(my_list)        # set로 바꿨다가 다시 list로 바꾸면 중복 제거 가능

################################################################################################

my_list = [1,2,3,4,5,5]
print(my_list)

my_dic = dict.fromkeys(my_list)        # 딕셔너리로 변환 (리스트의 순서는 보장하면서 중복값을 제거)
print(my_dic)

my_list = list(my_dic)            # 다시 딕셔너리를 리스트로 변환
print(my_list)        

################################################################################################





