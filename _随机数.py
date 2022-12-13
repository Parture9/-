# 创作者：陈德文
# 时 间：2022/12/11 18:45
import random

x = int(input("请输入你要的随机数个数:"))
for i in range(x):
    if i == x-1:
        print(random.randint(1, 43), end=" ")
    else:
        print(random.randint(1, 43), end=",")


