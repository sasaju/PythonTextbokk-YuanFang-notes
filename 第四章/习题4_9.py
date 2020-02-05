# 输出字符串中的数字
# 这一章的课后题还挺有意思 嘿嘿
# 我最开始想到的是正则表达式 不过按照课本的进度应该不会涉及到 
# 正则表达式方法我也写了出来 具体见 习题4_9_正则表达式.py
# 然后我就又想到了下面不是很pythonic的操作 字符串是随便打的没啥特别的意思 哈哈
message = "afdsf河北大学药学院贼六45药学加油235.447学药的有钱奥利给227772哈哈哈23333"
n = 0
yes = []
# 用列表存储所有数字和.的位置（下标）如不理解可以直接输出yes列表帮助理解
while n < len(message):
    if "0" <= message[n] <= "9" or message[n] == ".":
        yes.append(n)
    n += 1
# 如果位置是相连的就连续输出，如果位置有间隔就输出4个空格
for value in range(0, len(yes)):
    if value == 0:
        print(message[yes[0]], end="")
    elif yes[value] == yes[value-1]+1:
        print(message[yes[value]], end="")
    else:
        print("    ", end="")
"""
个人感觉我写的比答案简单hhhh
自我感觉甚是良好
"""
            
