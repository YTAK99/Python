rsp = ["가위", "바위", "보"]

'''
man1    man2
가위    가위    =   비김
가위    바위    <   man2
가위    보      >   man1
바위    가위    >   man1
바위    바위    =   비김
바위    보      <   man2
보      가위    <   man2
보      바위    >   man1
보      보      =   비김
'''

man1 = input()
man2 = input()

win_cases = [("가위", "보"), ("바위", "가위"), ("보", "바위")]

if man1 == man2:
    print("Result : Draw")

elif (man1, man2) in win_cases:
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")