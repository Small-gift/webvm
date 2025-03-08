# This Python code is a simple calculator that performs basic arithmetic operations based on user input.
if __name__ == '__main__':
    first_number = float(input("请输入第一个数字: "))  
    second_number = float(input("请输入第二个数字: "))  
    user_choice = int(input("请输入你的选择: (1.相加 2.相减 3.相乘 4.相除): ")) 

    if user_choice == 1:
        result = first_number + second_number
        print(f"答案为{result:.2f}")
    elif user_choice == 2:
        result = first_number - second_number
        print(f"答案为{result:.2f}")
    elif user_choice == 3:
        result = first_number * second_number
        print(f"答案为{result:.2f}")
    elif user_choice == 4:
        if second_number != 0:
            result = first_number / second_number
            print(f"答案为{result:.2f}")
        else:
            print("错误: 除数不能为零")
    else:
        print("无效的选择")
else:        
    print("欢迎使用计算器  @Zhi yuan版权所有")
    first_number = float(input("请输入第一个数字: "))  
    second_number = float(input("请输入第二个数字: "))  
    user_choice = int(input("请输入你的选择: (1.相加 2.相减 3.相乘 4.相除): ")) 

    if user_choice == 1:
        result = first_number + second_number
        print(f"答案为{result:.2f}")
    elif user_choice == 2:
        result = first_number - second_number
        print(f"答案为{result:.2f}")
    elif user_choice == 3:
        result = first_number * second_number
        print(f"答案为{result:.2f}")
    elif user_choice == 4:
        if second_number != 0:
            result = first_number / second_number
            print(f"答案为{result:.2f}")
        else:
            print("错误: 除数不能为零")
    else:
        print("无效的选择")