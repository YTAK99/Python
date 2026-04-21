# 문자열 콤마로 분리하여 출력 #

# 방법1

inp = input()
print(*inp, sep=",")

##########################

#방법2

inp = input()
print(",".join(inp))