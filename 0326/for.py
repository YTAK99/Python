for 변수 in 반복 범위 또는 대상:
    반복 수행 문자

for x in range(10):     # 0 이상 10 미만 (0~9)
    print('팔 벌려 뛰기 해')

for x in range(10):
    print(f'팔 벌려 뛰기 {x}회')

range(stop)     # 0 이상 stop 미만

for x in range(10):
    print(x)        # 0, 1, 2, ..., 9

range(start, stop)      # start 이상 stop 미만

range(1, 10)        # 1 이상 10 미만

range(start, stop, step)     # start 이상 stop 미만 step 만큼 증가

range(1, 10 ,2)     # 1 이상 10 미만 2씩 증가  => 1,3,5,7,9

range(2, 10 ,2)     # 2 이상 10 미만 2만큼 증가  => 2,4,6,8

range(3, 10 ,3)     # 3 이상 10 미만 3만큼 증가  => 3,6,9


for n in range (1, 31, 10):
    print(f'{n}번은 {n}번부터 {n+9}번까지 모아줘')



################################################################################################




#리스트, 튜플, 딕셔너리 활용

person = {'이름': '나귀욤', '나이':7, '키':120, '몸무게':23}

for v in person.values():
    print(v)
print('')

for k in person.keys():
    print(k)
print('')

for k, v in person.items():
    print(k, v)
print('')




print(*range(1,101))




dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))     # 9명 숫자를 입력받아 리스트 만들기기



a, b = [int(input()) for _ in range(2)]

for i in range(a, b-1, -1):
    print(i, end=' ')

################################################################################################



# 문자열





























