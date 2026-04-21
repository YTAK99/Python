# CH가 A안에 있다면 위치 출력
A = ['J', 'U', 'N', 'G', 'O','L']

CH = input()

if CH in A:
    print(A.index(CH))
else:
    print("none")