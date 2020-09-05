print("篮球记分系统：")
team1=["勇士队",0]
team2=['骑士队',0]
print("请输入球队名称和分数：格式为 ‘球队名-分数’,输入 ’game over‘ 结束")
while True:
    print("目前的两只队伍为勇士队和骑士队")
    inputstr=input()
    if inputstr=='game over':
        break
    inputstrs=inputstr.split("-")
    if len(inputstrs) !=2:
        print("请输入正确的格式")
        continue
    try:
        int(inputstrs[1])
    except ValueError:
        print("请输入正确的分数，分数为数字")
        continue
    if inputstrs[0]==team1[0]:
        team1[1]+=int(inputstrs[1])
    elif inputstrs[0]==team2[0]:
        team2[1]+=int(inputstrs[1])
    else:
        print("请输入正确的队伍名字")
        continue
    print('继续输入比分')
if team1[1]>team2[1]:
    print("winer is "+ team1[0])
else:
    print("winner is "+ team2[0])