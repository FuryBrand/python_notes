import pizza
#函数和类
#函数
# 8.1 定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()
# 8.1.1 向函数传递信息
def greet_to_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_to_user('jesse')
# 8.1.2 实参和形参
# 在函数greet_to_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信息。在代码greet_user('jesse')中，值'jesse'是一个实参。实
# 8.2 传递实参
# 8.2.1 位置实参 调用时参数的位置特别重要！！
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
# 8.2.2 关键字实参 不用特别关注参数位置
def describe_pet_keyword(animal_type, pet_name):
    """"显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet_keyword(animal_type='hamster', pet_name='harry')
# 8.2.3 默认值
# 注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。这让Python依然能够正确地解读位置实参。
def describe_pet_default(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet_default(pet_name='willie')
describe_pet_default('willie') # pet_name依然为位置实参，所以使用时可以不加上形参。
# 8.2.4 等效的函数调用
# 下面对这个函数的所有调用都可行：
# 一条名为Willie的小狗：
describe_pet_default('willie')
describe_pet_default(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet_default('harry', 'hamster')
describe_pet_default(pet_name='harry', animal_type='hamster')
describe_pet_default(animal_type='hamster', pet_name='harry')
# 8.2.5 避免实参错误
# 8.3 返回值
# 8.3.1 返回建单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician) #Jimi Hendrix
# 8.3.2 让实参变成可选 （可选参数默认值为空，然后函数中进行判断）
def get_formatted_full_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_full_name('jimi', 'hendrix')
print(musician) #Jimi Hendrix
musician = get_formatted_full_name('john', 'hooker', 'lee')
print(musician) #John Lee Hooker
# 8.3.3 返回字典
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician) #{'first': 'jimi', 'last': 'hendrix', 'age': 27}
# 8.3.4 结合使用函数和while循环
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
# 8.4 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
# 8.4.1 在函数中修改列表
# 相比于没有使用函数的版本，这个程序更容易扩展和维护。如果以后需要打印其他设计，只需再次调用print_models()即可。如果我们发现需要对打印代码进行修改，只需修改这些代码一次，就能影响所有调用该函数的地方；与必须分别修改程序的多个地方相比，这种修改的效率更高。
# 这个程序还演示了这样一种理念，即每个函数都应只负责一项具体的工作。第一个函数打印每个设计，而第二个显示打印好的模型；这优于使用一个函数来完成两项工作。编写函数时，如果你发现它执行的任务太多，请尝试将这些代码划分到两个函数中。别忘了，总是可以在一个函数中调用另一个函数，这有助于将复杂的任务划分成一系列的步骤。
# 8.4.2 禁止函数修改列表
# 为了不改变原有作为参数的列表可以将列表的副本传递给函数
# function_name(list_name[:])
# 但是若创建副本则需要消耗额外的时间和内存，请注意。
# 8.5 传递任意数量的实参
# 形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。函数体内的print语句通过生成输出来证明Python能够处理使用一个值调用函数的情形，也能处理使用三个值来调用函数的情形。它以类似的方式处理不同的调用，注意，Python将实参封装到一个元组中，即便函数只收到一个值也如此
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 8.6 将函数存储在模块中
#函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。import语句允许在当前运行的程序文件中使用模块中的代码。
#通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。
#导入模块的方法有多种，下面对每种都作简要的介绍。
# 8.6.1 导入整个模块
#pizza.py
def make_the_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
#making_pizzas.py
# import pizza #须在文件首进行引入
pizza.make_the_pizza(16, 'pepperoni')
pizza.make_the_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 8.6.2 导入特定的函数
# 你还可以导入模块中的特定函数，这种导入方法的语法如下：
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1, function_2
# 若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显式地导入了函数make_pizza()，因此调用它时只需指定其名称。
# 8.6.3 使用as给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名——函数的另一个名称，类似于外号。要给函数指定这种特殊外号，需要在导入它时这样做。
# from module_name import function_name as fn
# 8.6.4 使用as给模块指定别名
# 你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza指定别名p），让你能够更轻松地调用模块中的函数。相比于pizza.make_pizza()，p.make_pizza()更为简洁：
# import module_name as m
# 这样不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名。这些函数名明确地指出了函数的功能，对理解代码而言，它们比模块名更重要。
# 8.6.5 导入模块中的所有函数
# 使用星号（*）运算符可让Python导入模块中的所有函数：
# import语句中的星号让Python将模块pizza中的每个函数都复制到这个程序文件中。由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。
# 最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。这能让代码更清晰，更容易阅读和理解。这里之所以介绍这种导入方法，只是想让你在阅读别人编写的代码时，如果遇到类似于下面的import语句，能够理解它们：
# from module_name import *
# 8.7 函数编写指南
# 编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只在其中使用小写字母和下划线。描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵循上述约定。
# 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用它：他们完全可以相信代码如描述的那样运行；只要知道函数的名称、需要的实参以及返回值的类型，就能在自己的程序中使用它。
# 给形参指定默认值时，等号两边不要有空格：
# def function_name(parameter_0, parameter_1='default value')
# 对于函数调用中的关键字实参，也应遵循这种约定：
# function_name(value_0, parameter_1='value')
# PEP 8（https://www.python.org/dev/peps/pep-0008/）建议代码行的长度不要超过79字符，这样只要编辑器窗口适中，就能看到整行代码。如果形参很多，导致函数定义的长度超过了79字符，可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，从而将形参列表和只缩进一层的函数体区分开来。
# 大多数编辑器都会自动对齐后续参数列表行，使其缩进程度与你给第一个参数列表行指定的缩进程度相同：
def function_name(
    parameter_0, parameter_1, parameter_2,
    parameter_3, parameter_4, parameter_5):
    pass
# 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始。
# 所有的import语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。


# class
# 9.1 创建和使用类