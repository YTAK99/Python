# for x in range(1, X+1):
#     for y in range(1, X+1):
#         print(f'{x}/{y}', end=' ')
#     print()


'''   

1/1 (1)     1/2 (2)     1/3 (6)     1/4 (7)       1/5 (15)


2/1 (3)     2/2 (5)     2/3 (8)     2/4 (14)      2/5


3/1 (4)     3/2 (9)     3/3 (13)    3/4           3/5


4/1 (10)    4/2 (12)    4/3         4/4           4/5


5/1 (11)    5/2         5/3         5/4           5/5



1/1     1
1/2     2
2/1     3
3/1     4
2/2     5
1/3     6
1/4     7
2/3     8
3/2     9
4/1     10
5/1     11
4/2     12
3/3     13
2/4     14
1/5     15



right 1 -> left down 1 -> down 1 -> right up 2
right 1 -> left down 3 -> down 1 -> right up 4


b+1  ->  (a+1, b-1) X 1  ->  a+1  ->  (a-1,b+1) X 2     # 6번째     
b+1  ->  (a+1, b-1) X 3  ->  a+1  ->  (a-1,b+1) X 4     # 15번째    9
b+1  ->  (a+1, b-1) X 5  ->  a+1  ->  (a-1,b+1) X 6     # 28번째    13
b+1  ->  (a+1, b-1) X 7  ->  a+1  ->  (a-1,b+1) X 8     # 45번째    17
b+1  ->  (a+1, b-1) X 9  ->  a+1  ->  (a-1,b+1) X 10    # 66번째    21

'''




''' # 하다 말았다 #
X = int(input())

a = 1; b = 1       # 첫번째

X_count = 1

ww = 1; xx = 1; yy = 1; zz = 2

while True:
    if X == 1:
        break
    
    for w in range(1):
        b += 1
        X_count += 1
        if X == X_count:
            break
    
    for x in range(xx):
        a += 1;  b -= 1
        X_count += 1
        if X == X_count:
            break
    
    for y in range(1):
        a += 1
        X_count += 1
        if X == X_count:
            break
    
    for z in range(zz):
        a -= 1;  b += 1
        X_count += 1
        if X == X_count:
            break


print(f"{a}/{b}")
'''

X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    # 짝수 줄 (↗)
    a = X
    b = line - X + 1
else:
    # 홀수 줄 (↙)
    a = line - X + 1
    b = X

print(f"{a}/{b}")