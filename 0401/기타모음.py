# 문자열 붙여서
print(list(reversed(nums)))
'구분자'.join(리스트)


# 거꾸로
A = "apple orange banana"
print(*A.split()[::-1])



.split()     # 문자열 분리
.strip()     # 문자열 양쪽(앞뒤)의 공백을 제거




# 이중 리스트
i = [input().split() for _ in range(2)]

print(f"{i[0][0]}'s age - {i[1][0]}'s age = {int(i[0][1]) - int(i[1][1])}")




# 포함 범위
if all(-100 <= x <= 100 for x in (a, b, c)):




조건식 ? 참일 때 값 : 거짓일 때 값;

int a = 7, b = 3;
int min = (a < b) ? a : b;  // 결과: 3
printf("작은 값: %d\n", min);




a, b = map(int, open(0).read().split())


numbers = list(map(int, open(0).read().split()))
print(*numbers)








