# 文件和异常

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
