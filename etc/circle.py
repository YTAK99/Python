import turtle as k

k.setup(500, 500)
k.bgcolor('pink')
k.shape('classic')

k.title('원의 둘레 구하기 by 한영탁')
name = k.textinput('제목 입력', '문자로 입력하세요')
radius = k.numinput('반지름 입력','정수(1-150 사이)로 입력하세요')
girth = radius*2*3.14
k.pu()
k.goto(-50,200)
k.color("blue")
k.write(name, font=('굴림체', 20))                 #입력한 제목 출력하기
k.begin_fill()
k.fillcolor('skyblue')
k.pencolor('blue')
k.pensize('10')
k.goto(0,-radius)
k.pd()
k.speed(10)
k.circle(radius)                #입력한 반지름 크기로 원 그리기
k.end_fill()
k.pu()
k.goto(-200, -200)
k.color("red")
k.write('반지름 %d인 원의 둘레는 %d입니다.'%(radius, girth), font=('굴림체', 15))
k.hideturtle()              #거북이 모양 감추기
k.mainloop()
