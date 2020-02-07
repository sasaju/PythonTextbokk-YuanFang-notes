# 读取data_in.txt并将累加结果放在data_out.txt

with open('data_in.txt', 'r', encoding='utf-8') as datas:
    lines = datas.readlines()
    datas_sum = 0
    for line in lines:
        datas_sum += float(line)

with open('data_out.txt', 'w', encoding='utf-8') as out:
    out.write(str(datas_sum))
