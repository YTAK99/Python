[def]

def 함수명():
  수행할 문장


def 함수명(전달값):      # 전달값 : 여러 개 사용 가능 (콤마로 구분). 함수 내에서만 사용
  수행할 문장


########################################################################################################
    


def show_price():      # 함수 정의
    print(f'{customer} 고객님')
    print('감성 커트 가격은 15000 원입니다')

customer1 = '나장발'
print(f'사랑하는 {customer1} 고객님')
show_price() # 함수 호출

customer2 = '나수염'
print(f'사랑하는 {customer2} 고객님')
show_price() # 함수 호출


    

def show_price(customer):      # 전달값 넣어서 함수 정의
    print(f'사랑하는 {customer} 고객님')
    print('감성 커트 가격은 15000 원입니다')

customer1 = '나장발'
show_price(customer1) # 함수 호출

customer2 = '나수염'
show_price(customer2) # 함수 호출



########################################################################################################



def 함수명(전달값):
  수행할 문장
  return 반환값    # ↓↓ 호출했던 곳으로 반환값을 넘김 ↓↓    ◆ 반환값 : 여러 개 반환 가능 (콤마로 구분, 튜플), 반환되는 즉시 함수 탈출

함수명()



def get_price(is_vip): # True : 단골 손님, False : 일반 손님
  if is_vip == True:
    return 10000 # 단골 손님
  else:
    return 15000 # 일반 손님
price = get_price(True)
print(f'커트 가격은 {price} 원입니다') # 10000





########################################################################################################

[기본값 : 기본적으로 사용되는 값]


def 함수명(전달값=기본값):
  수행할 문장


{기존}

def get_price(is_vip=False): # True : 단골 손님, False : 일반 손님
  if is_vip == True:
    return 10000 # 단골 손님
  else:
    return 15000 # 일반 손님
price1 = get_price(True) # 단골 손님
price2 = get_price(False) # 일반 손님
price3 = get_price(False) # 일반 손님
price4 = get_price(False) # 일반 손님


{기본값 설정 후}

def get_price(is_vip=False): # True : 단골 손님, False : 일반 손님
  if is_vip == True:
    return 10000 # 단골 손님
  else:
    return 15000 # 일반 손님
price1 = get_price(True) # 단골 손님
price2 = get_price() # 일반 손님
price3 = get_price() # 일반 손님
price4 = get_price() # 일반 손님



############################################################################################################

[키워드값]


def get_price(is_vip=False, 
              is_birthday=False, # 때마침 생일이라면?
              is_membership=False,
              card=False,
              review=False,
              first_time=False):

price = get_price(review=True, is_birthday=True)      # 순서 무관하게 변경 가능



############################################################################################################



def order(shot=2, size='Regular', takeout=True): # 커피 주문
    print(f'아메리카노 {size} 사이즈 {shot}샷')
    if takeout:
        print('포장 주문이 완료되었습니다')
    else:
        print('주문이 완료 되었습니다')

order('Regular', takeout=True)      # 이렇게하면 -> 키워드를 명시하지 않아 의도치않게 shot의 전달값으로 들어감





############################################################################################################



def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2022년 6월 10일', '나장발') # 1명 방문
visit('2022년 6월 10일', '나장발', '나수염') # 2명 방문
visit('2022년 6월 10일', '나장발', '나수염', '나김리') # 3명 방문




############################################################################################################

[가변인자] : 전달값이 많으면 마지막에 한 번만

* <- asterisk 같은거










      
