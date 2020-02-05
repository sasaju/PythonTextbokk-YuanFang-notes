#b0106.py
#计算圆柱的表面积
PI = 3.14
r = float(input("半径="))
h = float(input("高度="))
a = 2*PI*r*r + 2*PI*r*h
print("表面积=",a)
