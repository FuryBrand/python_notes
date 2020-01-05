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
# 9.1.1 创建Dog类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
# 根据约定，在Python中，首字母大写的名称指的是类。这个类定义中的括号是空的，因为我们要从空白创建这个类。所以，我们编写了一个文档字符串，对这个类的功能作了描述。
# 方法__init__()
# 类中的函数称为方法；你前面学到的有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。__init__()是一个特殊的方法，每当你根据Dog类创建新实例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
# 我们将方法__init__()定义成了包含三个形参：self、name和age。在这个方法的定义中，形参self必不可少，还必须位于其他形参的前面。为何必须在方法定义中包含形参self呢？因为Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。我们创建Dog实例时，Python将调用Dog类的方法__init__()。我们将通过实参向Dog()传递名字和年龄；self会自动传递，因此我们不需要传递它。每当我们根据Dog类创建实例时，都只需给最后两个形参（name和age）提供值。
# 方法__init__()中定义的两个变量都有前缀self。以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量。self.name = name获取存储在形参name中的值，并将其存储到变量name中，然后该变量被关联到当前创建的实例。self.age = age的作用与此类似。像这样可通过实例访问的变量称为属性。Dog类还定义了另外两个方法：sit()和roll_over()。由于这些方法不需要额外的信息，如名字或年龄，因此它们只有一个形参self。我们后面将创建的实例能够访问这些方法，换句话说，它们都会蹲下和打滚。
# 当前，sit()和roll_over()所做的有限，它们只是打印一条消息，指出小狗正蹲下或打滚。但可以扩展这些方法以模拟实际情况：如果这个类包含在一个计算机游戏中，这些方法将包含创建小狗蹲下和打滚动画效果的代码。如果这个类是用于控制机器狗的，这些方法将引导机器狗做出蹲下和打滚的动作。
# 9.1.2 根据类创建实例并访问属性、调用方法
# 命名约定很有用：我们通常可以认为首字母大写的名称（如Dog）指的是类，而小写的名称（如my_dog）指的是根据类创建的实例。
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".") # My dog's name is Willie.
print("My dog is " + str(my_dog.age) + " years old.") # My dog is 6 years old.
my_dog.sit() # Willie is now sitting.
my_dog.roll_over() # Willie rolled over!
# 9.2 使用类和实例
# 9.2.1 Car类
# 参考下方代码
# 9.2.2 给属性指定默认值
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name()) # 2016 Audi A4
my_new_car.read_odometer() # This car has 0 miles on it.
# 9.2.3 修改属性的值（3种）
# 一、直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer() # This car has 23 miles on it.
# 二、通过方法修改属性的值，方法中可以加入额外的限制，具体看方法体
my_new_car.update_odometer(26) # This car has 26 miles on it.
my_new_car.update_odometer(22) # You can't roll back an odometer!
# 三、通过方法对属性的值进行递增
# 通过方法的改造，将属性赋值变为递增形式，而不是直接赋值
# def increment_odometer(self, miles):
#     """将里程表读数增加指定的量"""
#     self.odometer_reading += miles
# 9.3 继承
# 9.3.1 子类的方法__init__()
# 参考下方的代码
# 9.3.2 Python 2.7中的继承
# 在Python 2.7中，继承语法稍有不同，ElectricCar类的定义类似于下面这样：
# class Car27(object):
#     def __init__(self, make, model, year):
#         pass
# class ElectricCar27(Car27):
#     def __init__(self, make, model, year):
#         super(ElectricCar, self).__init__(make, model, year)
#         pass
# 函数super()需要两个实参：子类名和对象self。为帮助Python将父类和子类关联起来，这些实参必不可少。另外，在Python 2.7中使用继承时，务必在定义父类时在括号内指定object。
# 9.3.3 给子类定义属性和方法
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name()) # 2016 Tesla Model S
my_tesla.describe_battery() # This car has a 70-kWh battery.
# 9.3.4 重写父类的方法
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。
def fill_gas_tank():
    """电动汽车没有油箱"""
    print("This car doesn't need a gas tank!")
# 现在，如果有人对电动汽车调用方法fill_gas_tank()，Python将忽略Car类中的方法fill_gas_tank()，转而运行上述代码。使用继承时，可让子类保留从父类那里继承而来的精华，并剔除不需要的糟粕。
# 9.3.5 将实例用作属性
# 使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。你可以将大型类拆分成多个协同工作的小类。
# 例如，不断给ElectricCar类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。在这种情况下，我们可将这些属性和方法提取出来，放到另一个名为Battery的类中，并将一个Battery实例用作ElectricCar类的一个属性
# 9.3.6 模拟实物
# 较复杂的物件（如电动汽车）时，需要解决一些有趣的问题。续航里程是电瓶的属性还是汽车的属性呢？如果我们只需描述一辆汽车，那么将方法get_range()放在Battery类中也许是合适的；
# 但如果要描述一家汽车制造商的整个产品线，也许应该将方法get_range()移到ElectricCar类中。在这种情况下，get_range()依然根据电瓶容量来确定续航里程，但报告的是一款汽车的续航里程。
# 我们也可以这样做：将方法get_range()还留在Battery类中，但向它传递一个参数，如car_model；在这种情况下，方法get_range()将根据电瓶容量和汽车型号报告续航里程。
# 这让你进入了程序员的另一个境界：解决上述问题时，你从较高的逻辑层面（而不是语法层面）考虑；你考虑的不是Python，而是如何使用代码来表示实物。到达这种境界后，你经常会发现，现实世界的建模方法并没有对错之分。有些方法的效率更高，但要找出效率最高的表示法，需要经过一定的实践。
# 只要代码像你希望的那样运行，就说明你做得很好！即便你发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁；要编写出高效、准确的代码，都得经过这样的过程。
# 9.4 导入类
# 为遵循Python的总体理念，让文件尽可能整洁。Python允许你将类存储在模块中，然后在主程序中导入所需的模块。
# 9.4.1 导入单个类
# car.py中只有一个Car类
# from car import Car
# my_new_car = Car('audi', 'a4', 2016)
# 9.4.2 在一个模块中存储多个类
# car.py中有一个Car类一个Battery类以及一个ElectricCar(Car)。
# from car import ElectricCar
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# 9.4.3 从一个模块中导入多个类
# car.py中有一个Car类一个Battery类以及一个ElectricCar(Car)。
# from car import Car, ElectricCar
# my_beetle = Car('volkswagen', 'beetle', 2016)
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# 9.4.4 导入整个模块
# 你还可以导入整个模块，再使用句点表示法访问需要的类。这种导入方法很简单，代码也易于阅读。由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。
# import car
# my_beetle = car.Car('volkswagen', 'beetle', 2016)
# 9.4.5 导入模块中的所有类
# 不推荐，1，不知道导入了什么类，如果导入了同名类会比较麻烦。2.与其这样，不如直接导入整个模块，用module_name.class_name语法来访问类。可以避免冲突
# from module_name import *
# 9.4.6 在一个模块中导入另一个模块
# 有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。
# 9.4.7 自定义工作流程
# 正如你看到的，在组织大型项目的代码方面，Python提供了很多选项。熟悉所有这些选项很重要，这样你才能确定哪种项目组织方式是最佳的，并能理解别人开发的项目。
# 一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一切都能正确运行后，再将类移到独立的模块中。如果你喜欢模块和文件的交互方式，可在项目开始时就尝试将类存储到模块中。先找出让你能够编写出可行代码的方式，再尝试让代码更为组织有序。
# 9.5 Python标准库
# Python标准库是一组模块，安装的Python都包含它。
# 要创建字典并记录其中的键—值对的添加顺序，可使用模块collections中的OrderedDict类。OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。
# 9.6 类编码风格
# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。
# 实例名和模块名都采用小写格式，并在单词之间加上下划线。
# 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。
# 每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
# 可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
# 需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再添加一个空行，然后编写导入你自己编写的模块的import语句。在包含多条import语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方。
