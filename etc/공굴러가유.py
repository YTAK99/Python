from tkinter import Y
from turtle import *

def draw_arc(x):
    y = 40 * x -2 * (x ** 2)
    if y >= 0:
        goto(x * 30, y)
        write("(%d, %d)"%(x, y))
        stamp()
    return y

shape('classic')
sec = 1
while draw_arc(sec) > 0:
    sec += 1

print("공이 떨어지는 데 %d초 걸렸네요" %sec)