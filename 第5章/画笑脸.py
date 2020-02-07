import turtle

turtle.speed(100)
# 创建页面并画脸
turtle.setup(700, 700)
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.circle(300)

# 画左眼眼圈
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.circle(30)

# 画左眼眼球
turtle.penup()
turtle.sety(130)
turtle.pendown()
turtle.dot(10)

# 画右眼珠
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.circle(30)

# 画右眼球
turtle.penup()
turtle.sety(130)
turtle.pendown()
turtle.dot(10)

# 画嘴
turtle.penup()
turtle.goto(-160, -120)
turtle.pendown()
turtle.forward(320)
for i in range(-1600, 1610):
    turtle.goto(i/10, (i/10)**2/320-200)
    print(turtle.pos())


turtle.done()

