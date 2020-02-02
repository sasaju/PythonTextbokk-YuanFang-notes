#b0204.py   逆序输出值
"""
# 切片方法（可以倒序任何字符）
def order_str(str):
    return str[::-1]

str = input("str=")
ordered_str = order_str(str)
print(ordered_str)
"""
"""
# 答案的方法
n=int(input("n="))
m1=n%10
m2=n//10%10
m3=n//100
print(m1*100+m2*10+m3)
"""