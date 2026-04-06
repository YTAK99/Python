a = [1, 2, '삼', 'four']
b = ['BTS', '봉준호', '손흥민', '제이팍', 'Let`s go']

print(a[0])
print(a[0:2])
print('삼' in a)
print(len(a))

a[2] = '석삼'
print(a)

a.append('다섯')    # 값 추가
print(a)

a.remove(2)    # 값 삭제
print(a)

a.extend(b)     # 리스트 확장
print(a)

.split()     # 문자열 분리
.strip()     # 문자열 양쪽(앞뒤)의 공백을 제거

# insert()      # 원하는 위치에 값 추가
# pop()         # 원하는 위치 의 값 삭제
# clear()       # 모든 값 삭제
# sort()        # 값 순서대로 정렬렬  
# reverse()     # 순서 뒤집기
# copy()        # 리스트 복사
# count()       # 어떤 값이 몇 개 있는지
# index()       # 어떤 값이 어디에 있는지


# 문자열 붙여서
print(list(reversed(nums)))
'구분자'.join(리스트)


# 거꾸로
A = "apple orange banana"
print(*A.split()[::-1])



A = list(map(int, input().split()))
print(A)
