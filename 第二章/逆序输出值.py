#b0205.py   逆序输出值（方法很多，这里用切片实现）
def order_char(char):
    return char[::-1]

char = input("char=")
ordered_char = order_char(char)
print(ordered_char)
