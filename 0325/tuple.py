# 튜플 = (값1, 값2, ...) !수정불가! (=읽기 전용 리스트)

from itertools import count


tu = ('e', 'a', 'o', 'a')   # 중복 허용

print(tu[0])
print(tu[0:3])
print('a' in tu)
print(len(tu))

# count()       # 어떤 값이 몇 개 있는지
# index()       # 어떤 값이 어디에 있는지

(first, second, third, four) = tu       #언패킹
print(first)

(one, two, *others) = tu        # Asterisk
print(others)

(*others, another) = tu         # *others는 [ 리스트 형식으로 저장]
print(others)
