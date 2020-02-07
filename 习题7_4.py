# 异常
filepath = 'C:\\abc.txt'

try:
    with open(filepath) as f:
        text = f.read()
except FileNotFoundError:
    print("错误！文件不存在！")
except UnicodeDecodeError:
    print("请勿以Unicode编码格式保存文件！")
else:
    print(text)
