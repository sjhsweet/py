username = input('请输入您的用户名：')
while True:
    password1 = input('请输入您的密码：')
    password2 = input('请确认您的密码：')
    if password1 == password2:
        print('恭喜您，注册成功！')
        break
    else:
        print('两次密码输入不一致！')