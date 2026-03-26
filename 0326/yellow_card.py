yellow_card = 0
foul = False
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('후 조심해야제')
