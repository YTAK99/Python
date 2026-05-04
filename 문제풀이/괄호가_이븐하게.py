# 괄호가 (나왔으면  )가 나와서 ()가 완성되면 YES


T = int(input())

for _ in range(T):
    total = 0
    vps = input()

    for x in vps:
        if x == '(':
            total += 1
        elif x == ')':
            total -= 1

        if total < 0:
            break

    if total == 0:
        print("YES")
    else:
        print("NO")



#################################################################################


T = int(input())

for _ in range(T):
    total = 0
    is_vps = True
    vps = input()

    for x in vps:
        if x == '(':
            total += 1
        elif x == ')':
            total -= 1

        if total < 0:
            is_vps = False
            break

    if not is_vps or total != 0:
        print("NO")
    else:
        print("YES")


#################################################################################


def check():
    Str=input()

    while "()" in Str:
        Str = Str.replace("()","")
        
    if len(Str) == 0:
        print("YES")
    else :
        print("NO")

N = int(input())

for _ in range(N):
    check()

#################################################################################

# total = 0

# (가 나오면 total+=1 
# )가 나오면 total-=1

# 근데 중간에 한번이라도 total < 0 되면 탈락

T = int(input())

for _ in range(T):
    total = 0
    vps = input()
    boole = True
    
    for x in vps:
        if x == '(':
            total += 1
        elif x == ')':
            total -= 1

        if total < 0:
            print("NO")
            boole = False
            break
    
    if boole:        
        if total == 0:
            print("YES")
        else:
            print("NO")
