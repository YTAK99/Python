from random import sample

for x in range(5):
    numbers = list(range(1, 50))
    numbers = sample(numbers, 6)
    print("{0} : {1}".format(x+1, numbers))

input("종료하려면 엔터키를 누르세요...")
