#b0205.py   用到93页的字符串运算函数
str=input("str=")
print(chr(ord(str)+ord("a")-ord("A")))

"""
ord()是获得括号内字符的ASCII码
chr()是获得括号内ASCII码对应的字符
"""