num = input("请输入一个数字：")
while not num.isdigit():
    print("请输入一个整数")
    num = input("请重新输入一个数字：")
num = int(num)
while num > 1:
    if num%2 == 0:
        num //= 2
    else:
        num = num * 3 + 1
    print(num)
