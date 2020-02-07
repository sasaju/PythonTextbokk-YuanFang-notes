# 把诗句逐行输入文件
with open('poem.txt', 'a', encoding='utf-8') as p:
    p.write("八阵图\n")
    p.write("[唐]杜甫\n")
    p.write("功盖三分国，\n")
    p.write("名高八阵图。\n")
    p.write("江流石不转，\n")
    p.write("遗恨失吞吴。")
