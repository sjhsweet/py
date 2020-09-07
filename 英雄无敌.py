import math
import random
userdataname = ["admin","default"]
userdatapwd = ["123456","456789"]
name = "default"
pwd = "default"
def home():
    num = input("欢迎来到英雄无敌！\n请选择：1:注册     2:登录     ")
    if num == "1":
        signup_name()
    elif num == "2":
        login_name()
    else:
        print("选择错误！请重新选择：")
        home()
def signup_name():
    print("欢迎来到英雄无敌注册界面！")
    name = input("请输入您的角色名称：")
    while len(name) != 0 and len(name) <= 3 or len(name) > 9:
        name = input("您的角色名称长度不够，请重新输入您的角色名称：")
    while name in userdataname:
        name = input("角色名称已存在！请重新输入：")
        while len(name) != 0 and len(name) <= 3 or len(name) > 9:
            name = input("您的角色名称长度不够，请重新输入您的角色名称：")
    if not name:
        name = 'player' + str(random.randrange(101,199))
        print("检测到您未输入角色名称，我们将随机生成一个您的角色名称：",name)
        userdataname.append(name)
        signup_pwd()
    else:
        userdataname.append(name)
        signup_pwd()
def signup_pwd():
    pwd = input("请输入您的密码：")
    while 5 >= len(pwd) or len(pwd) > 10:
        pwd = input("您的密码长度不够，请重新输入您的密码：")
    print("注册成功，请返回主页面登录！")
    userdatapwd.append(pwd)
    home()
def login_name():
    print("欢迎来到英雄无敌登录界面！")
    username = input("请输入您的角色名称：")
    if username in userdataname:
        userindex = userdataname.index(str(username))
        login_pwd(userindex)
    else:
        print("您的角色不存在，将自动前往注册")
        signup_name()
def login_pwd(userindex):
    userpwd = input("请输入您的密码：")
    if userpwd == userdatapwd[userindex]:
        print("登录成功！")
        game(userindex)
    else:
        print("密码错误！")
        login_pwd(userindex)
def game(userindex):
    worknum = input("请选择您的英雄：1:法师，2:战士     ")
    mage = ("法师",100,100,80)
    warrior = ("战士",80,90,100)
    if worknum == "1":
        work = mage[0]
        hp = mage[1]
        attack = mage[2]
        defense = mage[3]
        print("%s选择成功" % work)
    elif worknum == "2":
        work = warrior[0]
        hp = mage[1]
        attack = warrior[2]
        defense = warrior[3]
        print("%s选择成功" % work)
    else:
        work = mage[0]
        hp = mage[1]
        attack = mage[2]
        defense = mage[3]
        print("默认英雄%s" % work)
    info = [work,hp,attack,defense]
    print("#    当前用户信息：            #")
    print("#    英雄名称：%-10s       #" % (info[0]))
    print("#    血值：%6d             #" % info[1])
    print("#    攻击力：%4d             #" % info[2])
    print("#    防御力：%4d             #" % (info[3]))
    map()
def map():
    worldMap = (['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#'])
    row = 0
    col = 0
    while 1:
        if row == -3 or row == 3:
            row = 0
        if col == -3 or col == 3:
            col = 0
        worldMap[col][row] = "*"
        print("当前您身处位置：")
        print("-"*9)
        print("$","".join(worldMap[0]),"$")
        print("$","".join(worldMap[1]),"$")
        print("$","".join(worldMap[2]),"$")
        print("-"*9)
        move = input("请输入wasd移动（按q退出游戏）：")
        if move == "w":
            worldMap[col][row] = '#'
            col -= 1
        elif move == "s":
            worldMap[col][row] = '#'
            col += 1
        elif move == "d":
            worldMap[col][row] = '#'
            row += 1
        elif move == "a":
            worldMap[col][row] = '#'
            row -= 1
        elif move == "q":
            break
        else:
            print("移动失败，请重新输入！")

home()