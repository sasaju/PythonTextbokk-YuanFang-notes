# 计算不及格的人数和
num_fail = num_good = 0
while True:
    grade = input("请输入成绩(输入q以离开)：")
    if grade == 'q':
        break
    elif int(grade) < 60:
        num_fail += 1
    elif int(grade) > 90:
        num_good += 1
print("不及格人数：", num_fail)
print("优秀人数：", num_good) 
