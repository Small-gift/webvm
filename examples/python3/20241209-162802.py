#问用户的年龄多少
user_age = int(input("请输入你的年龄: "))
if user_age > 100 or user_age <= 0:
    print("你的年龄不符合规范")
else:
    if user_age >= 18:
        print("你今年成年了")
    else:
        print("你今年没有成年")
    