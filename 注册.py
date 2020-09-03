username = input('请输入你的用户名：')
while True:
    password1 = input('请输入你的密码：')
    password2 = input('请再次输入你的密码：')
    if password1 == password2:
        print('恭喜您，注册成功，欢迎进入《英雄无敌》之英雄降临的世界……')
        break
    else:
        print('两次密码输入不一致！')

nickname = input ('请输入你的角色名称：')
race = input ('请输入你的种族：')
sex = input ('请输入你的性别：')
print ('你的信息如下：')
print (f'账号：{username}')
print (f'密码：{password1}')
print (f'角色名称：{nickname}')
print (f'性别：{sex}')
