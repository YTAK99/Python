dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))     # 9명 숫자를 입력받아 리스트 만들기기

total = sum(dwarfs)     # 전체 합 구하기

fake_found = False

for i in range(9):
    for j in range(i + 1, 9):
        # 만약 전체 합에서 두 명의 값을 뺐을 때 100이라면
        if total - dwarfs[i] - dwarfs[j] == 100:
            # 여기서 범인 두 명을 기억하거나 바로 처리
            fake1, fake2 = dwarfs[i], dwarfs[j]
            fake_found = True
            break
    if fake_found:
        break



# dwarfs 리스트에서 범인(fake1, fake2)를 제외한 나머지를 한 줄씩 출력
dwarfs.remove(fake1)
dwarfs.remove(fake2)
dwarfs.sort()

print(*dwarfs, sep='\n')







