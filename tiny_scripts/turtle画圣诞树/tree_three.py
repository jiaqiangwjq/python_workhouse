from turtle import *
import random
import time

t=Turtle()
t.up()
t.setx(200)
t.sety(-250)
t.down()
t.pencolor("grey")
t.write("By WJQ", font=("normal", 12, "italic")) #font-type有normal, bold, italic, underline

n = 80.0
 
speed("fastest")
screensize(bg='seashell')
time.sleep(7)
left(90)
forward(3*n)
color("orange", "red")
begin_fill()

left(126)

for i in range(5):
    forward(n/5)
    right(144)
    forward(n/5)
    left(72)
'''
right(90)
forward(n/6)
left(120)
forward(n/3)
left(120)
forward(n/3)
left(120)
forward(n/6)
'''
end_fill()
#left(90)
right(126)

color("dark green")
backward(n*4.8)
def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.5)
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)
tree(15, n)
backward(n/2)

for i in range(200):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if random.randint(0, 1) == 0:
            color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

time.sleep(5)