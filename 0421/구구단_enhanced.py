while True:
    s, e = map(int, input().split())
    if all(2 <= x <= 9 for x in (s, e)):
        break
    else:
        print("INPUT ERROR!")

# print(s, e)
    
for x in range(1, 10):
    if (s <= e):
        for y in range(s, e+1):
            print(f'{y} * {x} = {y*x:2d}', end ='   ')
        print()
    else:
        for y in range(s, e-1, -1):
            print(f'{y} * {x} = {y*x:2d}', end ='   ')
        print()


# for x in range(1, 10):
#     for y in range(8, 10):
#         print(f'{y} * {x} = {y*x:3d}', end ='   ')
#     print()