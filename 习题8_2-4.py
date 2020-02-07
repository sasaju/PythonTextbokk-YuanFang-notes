# Triangle类
class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        """使用海伦公式计算面积"""
        a = self.a
        b = self.b
        c = self.c
        self.p = (a+b+c) / 2
        p = self.p
        self.area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        print("面积：",self.area)
    
    def side(self):
        """直接计算周长"""
        a = self.a
        b = self.b
        c = self.c
        print("周长：", a+b+c)


class Pyramid(Triangle):
    def __init__(self, a , b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def vol(self):
        vol = self.area * self.h / 3
        print("体积：",vol)


demo = Pyramid(3, 4, 5, 5)
demo.area()
demo.side()
demo.vol()