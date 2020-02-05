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