# List : [] 중복O, 순서O, 수정O
# tuple : {} 중복O, 순서O, 수정X
# Set : () 중복X, 순서X

# 세트 = {값1, 값2, ...}  순서X, 중복X

A = {"돈가스", "보쌈", "제육덮밥"}
B = {"짬뽕", "초밥", "제육덮밥"}

print(A.intersection(B))        # A와 B의 교집합
print(A.union(B))       # A와 B의 합집합
print(A.difference(B))      # A - B 차집합

A.add('닭갈비')
print(A)

A.remove('제육덮밥')
print(A)

A.clear()
print(A)        # 모든 값 삭제

del A           # 완전 삭제
print(A)        # 그래서 없다고 나옴

'''
copy()      세트복사
discard()       값삭제(해당값이없어도에러발생X)
isdisjoint()        두세트에겹치는값이없는지여부
issubset()      다른세트의부분집합인지여부
issuperset()        다른세트의상위집합인지여부
update()        다른세트의값들을더함
'''
