# 答案先转成了列表，然后使用了列表的sort()方法对列表排序
# 我是直接把字典使用sorted()，两种方法都用了lambda函数，具体看代码最后面的注释

students = {
        "小明":{ "高等数学":78,"大学物理":82,"大学计算机":95,"大学英语":66 },
        "小花":{ "高等数学":51,"大学语文":67,"大学英语":45,"大学计算机":86 },
        "小莲":{ "大学数学":61,"大学计算机":65,"大学化学":87,"大学语文":91 },
        "小亮":{ "大学数学":72,"大学化学":52,"大学英语":81,"大学物理":88 },
    }
stu_dict = {}
for stu_name,stu_info in students.items():
    total_score = 0
    num = 0
    for course_name,course_score in stu_info.items():
        total_score += course_score
        num += 1
    ave_score=total_score // num
    stu_dict[stu_name] = ave_score
    stu_dict_orded = sorted(stu_dict.items(), key=lambda x:x[1],reverse=True) # 这行的解析在最下面
print(stu_dict_orded)

# 两种方法的输出略有不同，输出结果都是列表但列表的元素不同
# 答案输出的是[['小明', 80], ['小莲', 76], ['小亮', 73], ['小花', 62]]
# 我的输出是[('小明', 80), ('小莲', 76), ('小亮', 73), ('小花', 62)]
# 这与sorted的处理方法有关——sorted()会把键值转化为元组
"""
关于lambda函数：
lambda函数有很多种用法，有兴趣可以自行百度
对于第十九行：一定要注意sorted()的第一个参数一定要带.items()。
key=lambda x:x[1] 是指把元组中的第二个元素作为比较参数（答案中这一句的意思是把列表中下标为1的值作为比较参数）
reverse是正序反序的设置 默认为False（由小到大排列，升序），所以它的值设置为True（降序）
参考资料：https://www.runoob.com/python/python-func-sorted.html
"""