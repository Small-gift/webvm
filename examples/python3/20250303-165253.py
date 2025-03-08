import random
num = random.randint(1,100)

print("欢迎来到猜数字游戏")
print("数字范围在1到100内")
try:
    guess = int(input("请输入数字: "))
    while True:
        if guess == num:
            print("你猜对了")
            break;
        elif guess > num:
            print("你猜大了")
            guess = int(input("请输入数字: "))    
        elif guess < num:
            print("你猜小了")
            guess = int(input("请输入数字: "))
except ValueError:           
        print("输入为不合理数字，请重新运行程序，并输入正确的数字")