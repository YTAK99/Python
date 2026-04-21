# 연속 증가 리스트 인지 판단
N = int(input())

lst = []
backnum = 0

for _ in range(N):
    inp = int(input())
    lst.append(inp)

for x in lst:
    if x > backnum:
        backnum = x
    else:
        print("NO")
        break
else:       # for~else : break 안 걸리면 else 실행
    print("YES")