class Pname:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def Info():


peopleName = []
peopleAge = []

N = int(input())

for x in range(N):
    n, a = input().split()
    peopleName.append(n)
    peopleAge.append(a)

peopleName.sort(reverse=True)
peopleAge.sort(reverse=True)

for x in range(N):
    print(f'Name:{peopleName[x]}, Age:{peopleAge[x]}')



###########################################################

class Pname:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

N = int(input())

people = []

for _ in range(N):
    n, a = input().split()
    people.append(Pname(n, a))

people.sort(key=lambda x: x.age, reverse=True)

for p in people:
    print(f"Name:{p.name}, Age:{p.age}")
