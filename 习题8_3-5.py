# 定义学生类
class Student():
    def __init__(self, id, year, sc1, sc2, sc3):
        self.id = id
        self.year = year
        self.sc1 = sc1
        self.sc2 = sc2
        self.sc3 = sc3
    
    def averange(self):
        """计算平均值"""
        self.sum = self.sc1 + self.sc2 + self.sc3
        pingjun = self.sum / 3
        return pingjun
    
    def max_sc(self):
        """计算最大值"""
        max_sc = max(float(self.sc1), float(self.sc2), float(self.sc3))
        return max_sc

    def __add__(self, other):
        """运算符重载实现需求"""
        if self.id == other.id and self.year == other.year:
            return Student(self.id, self.year,self.sc1+other.sc1, 
                self.sc2+other.sc2, self.sc3+other.sc3)
        else:
            print("不是一个人，无法相加！")



demo1 = Student(20191801000,20,90,91,93.5)
demo2 = Student(20191801000,20,1,2,3.5)
print(demo1.averange())
print(demo1.max_sc())

# 两个数据相加
demo3 = demo1 + demo2
print(demo3.averange())
print(demo3.max_sc())
