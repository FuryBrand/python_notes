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
print(musician)
# 8.3.2 让实参变成可选 （可选参数默认值为空，然后函数中进行判断）
def get_formatted_full_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
# 8.3.3 返回字典
