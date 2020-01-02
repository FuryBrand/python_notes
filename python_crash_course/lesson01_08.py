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