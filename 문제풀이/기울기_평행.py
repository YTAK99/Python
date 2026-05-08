# 점들이 들어있는 리스트를 받고 선분을 만들어서 두 직선이 평행한 경우 1 반환

def solution(dots):

    def slope(a, b):
        return (b[1] - a[1]) / (b[0] - a[0])

    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1

    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1

    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1

    return 0

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))

result = solution([[3, 5], [4, 1], [2, 4], [5, 10]])
print(result)
