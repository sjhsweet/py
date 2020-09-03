import random
s = random.randint(1,100)
print(s)
num = int(input("请输入一个100以内的数字（10次机会）："))
times = 10
i = 1
while i < times:
    if num == s:
        print("恭喜你！用了%s次就猜对了！" % i)
        break
    elif num > s:
        print("很抱歉，猜的数字大了些，还有%s次机会" % (times - i))
        num = int(input("请重新输入："))
    else:
        print("很抱歉，猜的数字小了些，还有%s次机会" % (times - i))
        num = int(input("请重新输入："))
    i+=1