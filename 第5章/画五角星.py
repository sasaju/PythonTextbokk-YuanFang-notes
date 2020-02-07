# 画五角星
import turtle

def oneside():
    """划条线所需的操作"""
    turtle.pendown()
    turtle.right(144)   # 小王八头部顺时针旋转144°
    turtle.forward(400)

turtle.setup(1000, 700)
turtle.penup()          # 抬起笔来
turtle.goto(200,30)
turtle.pencolor("red")  # 将笔的颜色设为红色
turtle.fillcolor("red") # 将填充颜色设为红色

turtle.begin_fill()     # 开始填充准备
for _ in range(5):
    """每次画出一条边循环五次"""
    oneside()
turtle.end_fill()
turtle.penup()

turtle.goto(-250, 200)
turtle.write("红色五角星", font=("宋体", 80, "normal"))    # 打印红色五角星字样
turtle.hideturtle()     # 隐藏小王八

turtle.done()           # 让小王八画完之后不关闭
