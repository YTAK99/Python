a,b = input().split()
print(a, b)

def change_loc(pa, pb):
    a, b = pb, pa
    print(f'함수 내부: a = {a}, b = {b}')

change_loc(a, b)
print(f'함수 외부: a = {a}, b = {b}')

change_loc(a, b)
print(f'함수 외부: a = {a}, b = {b}')