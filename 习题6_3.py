# 逐行输出诗句
with open('poem.txt', 'r', encoding='utf-8') as p:
    for _ in range(6):
        line = p.readline()
        print(line.rstrip())
