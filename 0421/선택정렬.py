# 선택정렬 - 기준값보다 작은 게 나타나면 그때그때 자리를 바꾼다

A = [3, 5, 2, 1, 4]

for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        # 현재 기준(i)보다 더 작은 값을 발견하면 즉시 교환
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            
    # 한 회차(i)가 끝날 때마다 출력
    print(A)