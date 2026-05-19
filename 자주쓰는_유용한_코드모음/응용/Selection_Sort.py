# 선택 정렬이란 내부정렬 알고리즘의 하나로 다음 순서대로 실행하여 정렬을 한다.

# 1. 주어진 수열 중에 최소값(같은 값이 여러 개 있는 경우 처음 값)을 찾는다.
# 2. 찾은 최소값을 맨 앞의 값과 자리를 바꾼다.
# 3. 맨 앞의 값을 뺀 나머지 수열을 같은 방법으로 전체 개수-1번 반복 실행한다.


def selection_sort(lst, N):
    for i in range(N - 1):
        min_idx = i  # 현재 위치를 최소값으로 가정

        for j in range(i + 1, N):
            if lst[j] < lst[min_idx]:

                min_idx = j

        # swap
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        print(*lst)


N = int(input())
lst = list(map(int, input().split()))

selection_sort(lst, N)



# n=int(input())
# l=list(map(int,input().split()))
# for i in range(len(l)-1):
#     m=l[i:].index(min(l[i:]))+i
#     l[m],l[i] = l[i],l[m]
#     print(*l)
