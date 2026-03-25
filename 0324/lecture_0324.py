lang = 'PYTHON'
print(lang[0])
print(lang[-1])
print(lang[:3])
print(lang[2:])
print(lang[:])

num = 3
num += 2    #num = num + 2
print(num)

num -= 1
num *= 2
num /= 4
print(num)

snack = '꿀꽈배기'
print(len(snack))

snack = '''꿀꽈배기는
너무
맛있어요'''
print(snack)

print('-' * 10)
print('NadoCoding')
print('*' * 20)
print('100\n'*10)

let = 'hOw aRe yOu?'
print(let.lower())  # 전체 소문자로
print(let.upper())  # 전체 대문자로
print(let.capitalize())  # 전체 중에 첫 문자만 대문자로
print(let.title())  # 각 단어의 첫 문자만 대문자로
print(let.swapcase())  # 대소문자 상호 변환
print(let.split())  # 문자열 배열로 분리 (공백이 구분자)
print(let.count('O'))   # ' ' 안의 문자가 몇번 쓰였는지

s = '나도고등학교'
print(s.startswith('나도')) # '나도'로 시작하는지 확인
print(s.endswith('초등학교')) # '학교'로 끝나는지 확인

s2 = '.,.나도고등학교,..'
print(s2.strip('.'))    # '.' 앞뒤의 문자를 제거
print(s2.replace('고등학교교', '고교'))     # 단어 바꾸기

print(s.find('학교'))       # 단어의 위치를 찾음
print(s.find('g'))      # 없을 경우 -1

print(s.center(10,'-'))     # 다른 문자들 사이 가운데
