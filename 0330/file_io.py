open(파일명, 열기 모드, encoding='인코딩')

< 열기 모드 >
r : read (읽기)
w : write (쓰기)
a : append (이어서 쓰기)


f open('example.txt', 'w', encoding='utf8') # 쓰기 모드로 파일 열기
f.write('김xx\n') # 문장 입력하기
f.write('정xx\n') # 문장 입력하기
f.write('허xx\n') # 문장 입력하기
f.close() # 파일 닫기       (반드시)


f = open('example.txt', 'r', encoding='utf8') # 쓰기 모드로 파일 열기
contents = f.read()     # 파일 내용 다 읽어오기
print(contents)


f = open('example.txt', 'a', encoding='utf8') # 이어서 쓰기
f.write('김xx\n') # 문장 입력하기
f.write('정xx\n') # 문장 입력하기
f.write('허xx\n') # 문장 입력하기
f.close() # 파일 닫기       (반드시)



for line in f:
    print(line, end='')     # 한 줄씩 읽기기
f.close()


with        # 블럭 벗어나면 자동으로 파일 닫음


with openopen('example.txt', 'a', encoding='utf8') as f:        # with 파일 쓰기
f.write('김xx\n') # 문장 입력하기
f.write('정xx\n') # 문장 입력하기
f.write('허xx\n') # 문장 입력하기
f.close() # 파일 닫기


with open('example.txt', 'a', encoding='utf8') as f:            #with 파일 읽기
contents = f.read()
print(contents)



