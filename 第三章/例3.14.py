# 判断[2,2000]内质数的个数
num = 0
for n in range(2, 21):
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "不是质数")
            break     
    else:
        num += 1
        print(n, "是质数")
print("素数的个数=", num)
# 课本上的=和==以及其他运算符的两侧竟然都没有空格emmm...
# PEP8的要求是这种情况是要加的，不过并不影响能不能运行。
# 我觉得加上好看，不然代码看起来就像拧在一起的 /抠鼻