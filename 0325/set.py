# List : [] 중복O, 순서O, 수정O
# tuple : {} 중복O, 순서O, 수정X
# Set : () 중복X, 순서X

# 세트 = {값1, 값2, ...}  순서X, 중복X

A = {"돈가스", "보쌈", "제육덮밥"}
B = {"짬뽕", "초밥", "제육덮밥"}

print(A.intersection(B))        # A와 B의 교집합
print(A.union(B))       # A와 B의 합집합
print(A.difference(B))      # A - B 차집합
