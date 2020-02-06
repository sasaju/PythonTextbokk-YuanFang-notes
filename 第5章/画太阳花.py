# 这是turtle官方文档的例子
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:  # 小王八的位置到原点的距离小于1，其实就是回到了原点
        break
end_fill()
done()