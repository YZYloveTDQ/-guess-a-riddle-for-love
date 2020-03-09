import turtle as t
import random
import time


# --------------密码--------------------------------
str = t.textinput ("""小可爱，你能猜中这个小谜语么？""","""老婆，你觉得一年之中的哪一天的数字最好看？(格式：0229)""")
response = ["这个日子我也很喜欢的，可是并不是我最喜欢的哟~",
            "哎呀~动动你可爱的小脑袋呀！",
            "很接近了哦，嘻嘻，再猜再猜",
            "还没猜出来，哼！",
            "老婆加油，想想还有哪个日子是我最喜欢的",
            "我最喜欢的肯定跟你有关呀",
            "和你有关的日子就这么多呀",
            "我是不会告诉你答案的"]

while str != '0629':
    i = random.randint(0, 6)
    str = t.textinput("猜错了", response[i])

# ------------画布-----------------------------------
t.setup(width=800, height=600)

# ---------------图画部分---------------------------
t.pencolor('black') # 画笔颜色
t.speed(2)

"""右侧身体"""
t.pensize(6)
t.hideturtle()
t.penup()
t.goto(80, -200)
t.left(30)
t.circle(220, 10)
t.right(90)
t.showturtle()
t.pendown()
t.circle(-200, 20)

"""头部"""
t.pensize(4)
t.hideturtle()
t.penup()
t.goto(80, -200)
t.seth(0)
t.left(30)
t.pendown()
t.circle(220, 300)

"""眼睛"""
t.penup()
t.hideturtle()
t.goto(-150, 100)
t.left(20)
t.showturtle()

t.pensize(8)
t.pendown()
t.circle(-200,21)
t.forward(10)
t.pensize(6)
t.right(150)
t.circle(220, 25)

t.hideturtle()
t.penup()
t.goto(100, 90)
t.showturtle()
t.pendown()

t.pensize(8)
t.right(20)
t.circle(200, 20)
t.forward(20)
t.pensize(6)
t.left(150)
t.circle(-200, 20)
t.forward(20)

"""鼻子"""
t.penup()
t.hideturtle()
t.goto(-70, 20)
t.showturtle()
t.pensize(2)
t.pendown()

t.right(90)
t.forward(7)
t.circle(10, 180)
t.forward(10)
t.right(150)
t.forward(10)
t.circle(20, 200)

"""腮红"""
t.penup()
t.pensize(2)
t.hideturtle()
t.goto(-200, 10)
t.showturtle()
t.pencolor('red')
t.left(120)
t.speed(3)

for i in range(4):
    t.pendown()
    t.forward(50+i*7)
    t.penup()
    t.hideturtle()
    t.goto(-200+i*10, 10-i*0.9)

for i in range(6):
    t.pendown()
    t.forward(71-i*2)
    t.penup()
    t.hideturtle()
    t.goto(-170+i*10, 7.3-i)

t.hideturtle()
t.goto(50, 2)
t.showturtle()

for i in range(6):
    t.pendown()
    t.forward(71-i*2)
    t.penup()
    t.hideturtle()
    t.goto(50+i*10, 2-i)

for i in range(4):
    t.pendown()
    t.forward(61+i*2)
    t.penup()
    t.hideturtle()
    t.goto(110+i*10, -4-i)

t.pencolor('black')
t.pensize(6)
t.hideturtle()
t.goto(-170, -180)
t.right(90)
t.showturtle()
t.pendown()
t.circle(200, 25)

t.penup()
t.hideturtle()
t.goto(-250, -160)
t.right(110)
t.showturtle()
t.pendown()
t.circle(20, 280)
t.forward(5)
t.right(20)
t.forward(80)

# 手指
t.pensize(6)
t.penup()
t.hideturtle()
t.goto(-250, -140)
t.left(100)
t.showturtle()
t.pendown()
t.circle(200, 5)
t.circle(5,160)
t.forward(15)

# 爱心
def heart():
    t.pensize(3)
    t.left(135)
    t.forward(30)
    t.right(180)
    t.circle(10, -180)
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.circle(-10, 180)
    t.forward(30)

t.penup()
t.hideturtle()
t.goto(-320, -80)
t.seth(0)
# t.showturtle()
t.pendown()
r = random.random()
g = random.random()
b = random.random()
t.fillcolor((r, g, b))
t.begin_fill()
heart()
t.hideturtle()
t.end_fill()

# ----------------上部分文字------------------------
t.hideturtle() # 隐藏画笔
t.pencolor('red')
t.pensize(3)
t.penup() # 抬起画笔，不用轨迹
t.goto(-250, 200) # 指定位置

words1 = ['老',' 婆',' 你',' 真',' 棒!']
for i in range(5):
    t.write(words1[i], font=('华文彩云', i*10+20))
    time.sleep(0.5)
    t.forward(40+i*10)

# ---------------
t.pencolor('black')
for i in range(100):
    t.penup()
    t.hideturtle()
    t.goto(-320, -80)
    t.seth(0)
    # t.showturtle()
    t.pendown()
    r = random.random()
    g = random.random()
    b = random.random()
    t.fillcolor((r, g, b))
    t.begin_fill()
    heart()
    t.hideturtle()
    t.end_fill()
    t.undo()
    time.sleep(0.5)

t.done()










    
    
