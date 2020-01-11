# 文件、异常和测试

import json
# 10.1 从文件中读取数据
# 10.1.1 读取整个文件
with open('./python_crash_course/attach/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
# open()函数，用于打开某一文件并以file_object表示这个文件对象。
# with关键字，使用它可以在不再需要访问文件后python自动将其关闭，以避免错误。同时也可以用close()函数来关闭，但是在程序有bug的情况下不安全。
# 10.1.2 文件路径
# Linux和OS X中路径分隔符用/（斜杠）
# Windows中用\（反斜杠）
# 注意：Windows系统有时能够正确地解读文件路径中的斜杠。如果你使用的是Windows系统，且结果不符合预期，请确保在文件路径中使用的是反斜杠。另外，由于反斜杠在Python中被视为转义标记，为在Windows中确保万无一失，应以原始字符串的方式指定路径，即在开头的单引号前加上r。
# 10.1.3 逐行读取
filename = r'.\python_crash_course\attach\pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # 由于文本中本身包含换行且print也会换行，所以干掉一个换行
# 10.1.4 创建一个包含文件各行内容的列表
# 使用with时，open()返回的对象只能在with代码块内可用。所以将其保存到列表中为后续使用做准备。
filename = r'.\python_crash_course\attach\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
# 10.1.5 使用文件的内容
filename = r'.\python_crash_course\attach\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string) # 3.141592653589793238462643383279
print(len(pi_string)) # 32
# 10.1.6 包含一百万位的大型文件
# 对于你可处理的数据量，Python没有任何限制；只要系统的内存足够多，你想处理多少数据都可以。
# 10.1.7 圆周率值中包含你的生日吗
filename = r'.\python_crash_course\attach\pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# 10.2 写入文件
# 10.2.1 写入空文件
filename = './python_crash_course/attach/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
# w（写入模式）r（读取模式）a（附加模式）r+（读取和写入模式）
# 默认是r
# 注意：Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。
# 10.2.2 写入多行 （\n换行符）
filename = './python_crash_course/attach/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
# 10.2.3 附加到文件
filename = './python_crash_course/attach/programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    
# 10.3 异常
# 10.3.1 处理ZeroDivisionError异常
# print(5/0)
"""
Traceback (most recent call last):
  File "xixi.py", line 1, in <module>
    print(5/0)
ZeroDivisionError: division by zero
"""
# 10.3.2 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# 10.3.3 使用异常避免崩溃
# 程序崩溃可不好，但让用户看到traceback也不是好主意。不懂技术的用户会被它们搞糊涂，而且如果用户怀有恶意，他会通过traceback获悉你不希望他知道的信息。例如，他将知道你的程序文件的名称，还将看到部分不能正确运行的代码。有时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。
# 10.3.4 else代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
# try-except-else代码块的工作原理大致如下：Python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try语句中。有时候，有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else代码块中。except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。
# 10.3.5 处理FileNotFoundError异常
filename = 'alice.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
"""
Traceback (most recent call last):
  File "xixi.py", line 2, in <module>
    with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
"""
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
# 10.3.6 分析文本
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
# 10.3.7 使用多个文件
# 将上一节的代码包装成一个方法，进行多次调用。
# 在这个示例中，使用try-except代码块提供了两个重要的优点：
# 1.避免让用户看到traceback；
# 2.让程序能够继续分析能够找到的其他文件。如果不捕获因找不到siddhartha.txt而引发的FileNotFoundError异常，用户将看到完整的traceback，而程序将在尝试分析 Siddhartha 后停止运行——根本不分析 Moby Dick 和 Little Women。
# 10.3.8 失败时一声不吭
# 在except止呕使用pass来忽略错误
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
# 10.3.9 决定报告那些错误

# 10.4 存储数据
# JSON来分享数据。JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见格式，被包括Python在内的众多语言采用。
# 10.4.1 使用json.dump()和json.load()
# 将数据以JSON的形式写入到文件中
#import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
# 从文件中读取JSON
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
# 10.4.2 保存和读取用户生成的数据
# import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
# 10.4.3 重构
# 代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。这样的过程被称为重构。
# 重构让代码更清晰、更易于理解、更容易扩展。
# 上一节的代码可以重构成3个方法。

# 11.1 测试函数
# 11.1.1 单元测试和测试用例
# Python标准库中的模块unittest提供了代码测试工具。单元测试用于核实函数的某个方面没有问题；
# 测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。
# 全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。对于大型项目，要实现全覆盖可能很难。通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。
# 11.1.2 可通过的测试
# 参考codes下的test_name_function.py。
# 11.1.3 不能通过的测试
# 随便改改让它报错就行了。
# 11.1.4 测试未通过时怎么办
# 改呗，如果测试用例没问题的话，那自然是源码的问题。
# 11.1.5 添加新测试
# 在原来的文件的类中继续增加新的方法就行了

# 11.2 测试类
# 11.2.1 各种断言方法
# 常见的6种断言：
# assertEqual(a, b) # 核实a == b
# assertNotEqual(a, b) # 核实 a != b
# assertTrue(x) # 核实x为True
# assertFalse(x) # 核实x为False
# assertIn(item, list) # 核实item在list中
# assertNotIn(item, list) #核实item不在list中
# 11.2.2 一个要测试的类
# ./codes/survey.py是提供基础服务的类
# ./codes/language_survey.py是使用的类
# 11.2.3 测试AnonymousSurvey类
# ./codes/test_survey.py是测试基础服务的类。参考class TestAnonymousSurvey(unittest.TestCase)
# 11.2.4 方法setUp()
# 如果你在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。从而提取通用的东西来减少编码重复。
# ./codes/test_survey.py。参考class TestAnonymousSurveyPlus(unittest.TestCase):

# 11.3 小结

