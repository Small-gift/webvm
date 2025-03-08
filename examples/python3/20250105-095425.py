keyWord = {
    "输出": "print",
    "输入": "input",
    "如果": "if",  # 条件判断
    "否则": "else",  # 条件分支
    "如否": "elif",  # 条件分支
    "并且": "and",  # 逻辑与
    "或者": "or",  # 逻辑或
    "继续": "continue",  # 跳过当前循环
    "不是": "not",  # 逻辑非
    "是的": "is",  # 比较对象"假的": "False",  # 布尔值假
    "真的": "True",  # 布尔值真
    "空值": "None",  # 空值
    "断言": "assert",  # 断言"迭代": "for",  # 迭代循环
    "中断": "break",  # 退出循环
    "循环": "while",  # 条件循环
    "跳过": "pass",  # 空操作
    "在内": "in",  # 成员检查
    "匹配": "match",  # 模式匹配
    "情况": "case",  # 模式匹配的分支"函数": "def",  # 函数定义
    "类别": "class",  # 类定义
    "返回": "return",  # 返回值"导入": "import",  # 导入模块
    "作为": "as",  # 模块别名
    "起始": "from",  # 从模块导入
    "删除": "del",  # 删除对象
}

code = """
# This Python code is a simple calculator that performs basic arithmetic operations based on user input.
try:
    first_number = int(输入("请输" + "入第一个数字: "))  
    second_number = int(输入("请输" + "入第二个数字: "))  
    user_choice = int(输入("请输" + "入你的选择: (1.相加 2.相减 3.相乘 4.相除): "))
except ValueError:
如果 user_choice == 1:
    result = first_number + second_number
    输出("答案为" + format(result))
如否 user_choice == 2:
    result = first_number - second_number
    输出("答案为" + format(result))
如否 user_choice == 3:
    result = first_number * second_number
    输出("答案为" + format(result))
如否 user_choice == 4:
    如果 second_number != 0:
        result = float(first_number) / second_number
        输出("答案为" + format(result))
    否则:
        输出("错误: 除数不能为零")
否则:
    输出("无效的选择")
"""

for key in keyWord:
    code = code.replace(key,keyWord[key])
exec(code)
    