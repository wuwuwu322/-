key=input("请设置您的密码：")
i=1
print("即将进行登陆操作.......")
while i<=3:
    print("请输入您的密码：")
    searchkey=str(input())
    if(searchkey==key):
        print("恭喜你，密码输入正确，可以进入登陆页面........")
        break
    else:
        print("很抱歉，您输入的代码有误，您还剩下",+3-i,"次机会..........")
        i=i+1

if(i>3):print("很遗憾，您将无法在今日继续进行登陆操作，请明天再来吧")

