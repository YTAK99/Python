def bubble_sort(lst, N):
    for i in range(N-1):     # 바깥 루프 (회전 횟수)
        for j in range(N-1-i):     # 안쪽 루프 (비교). 매번 비교 범위가 줄어든다.
                                       # -i : 이미 뒤쪽은 정렬 완료돼서 비교 범위 축소
            if lst[j] > lst[j+1]:     # 인접한 두개 비교해서 (오름차순 기준)
                lst[j], lst[j+1] = lst[j+1], lst[j]     # 큰 값을 오른쪽으로 밀어냄 (교환)
        print(lst)

N = int(input())
lst = list(map(int, input().split()))

bubble_sort(lst, N)

# 1. --------------------------------

#bubble sort
N = int(input())
lst = list(map(int, input().split()))

# print(lst)
isSorted = True

while isSorted:
    isSorted = False
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            tmp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = tmp
            isSorted = True
    if isSorted == True:
        print(lst)
