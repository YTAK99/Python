import datetime

name = input()
age = int(input())

current_year = datetime.datetime.now().year

print(f'{name}(은)는 {current_year + (100 - age)}년에 100세가 될 것입니다.')
