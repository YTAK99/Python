lst = [1, 1, 2, 3, 2, 1, 4, 5, 6, 4]

중복있는거 = []     # duplicate
중복없는거 = []     # seen

for num in lst:
    if num not in 중복없는거:
        중복없는거.append(num)
    else:
        if num not in 중복있는거:
            중복있는거.append(num)

print("노중복:", 중복없는거)
print("예스중복:", 중복있는거)
