yellow_card = 0
foul = True        # False면 아무것도 X
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('후 조심해야제')

################################################################################################

yellow_card = 1
foul = 1
if foul == 1:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('후 조심해야제')
