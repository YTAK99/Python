max = num1 if num1 > num2 else num2      # 앞의 두수 중에서 큰값을 max에 넣기
max = num3 if num3 > max else max        # max와 마지막 수에서 큰값을 max에 넣기

min = num1 if num1 < num2 else num2      # 앞의 두수 중에서 작은값을 max에 넣기
min = num3 if num3 < min else min        # min과 마지막 수에서 작은값을 min에 넣기

print('최대값은 {0}입니다.'.format(max))
print('최소값은 {0}입니다.'.format(min))
