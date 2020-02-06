# 我是头一次见先定义函数再引入第三方库的 除了除非有注释 否则import一般在开头的
# turtle库画正方形
import turtle

def draw(x, y, fd):
    """x为起始位置，y为终止位置，fd为边长"""
    turtle.goto(x, y)
    turtle.pendown()    # 落笔
    for i in range(4):
        """画出四个边"""
        turtle.forward(fd)
        turtle.right(90)
    turtle.penup()  # 抬笔

turtle.setup(500, 350, 325, 175)
turtle.pencolor("red")
turtle.pensize(1)
square_x = -2
square_y = 2
length = 5
for k in range(20):
    draw(square_x, square_y, length)
    square_x -= 5
    square_y += 5
    length += 10
turtle.done()   # 这一句可以使小王八画完之后不关闭
