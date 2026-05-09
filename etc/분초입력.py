total_sec = 0

while True:
    data = input("분 초 입력: ")

    if data == "0":
        break

    minute, second = map(int, data.split())

    total_sec += minute * 60 + second

hour = total_sec // 3600
minute = (total_sec % 3600) // 60
second = total_sec % 60

print(f"{hour}시간 {minute}분 {second}초")
