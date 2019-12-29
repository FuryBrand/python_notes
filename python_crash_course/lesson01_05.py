# if
# 5.2 条件测试，每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。
# 5.2.1 检查是否相等
# 这个相等运算符“==”在它两边的值相等时返回True，否则返回False。
# 5.2.2 检查是否相等时不考虑大小写
car = 'Audi'
print(car.lower() == 'audi') #True
# 5.2.3 检查是否不相等
# 要判断两个值是否不等，可结合使用惊叹号和等号（!=），其中的惊叹号表示不，在很多编程语言中都如此。
# 5.2.4 比较数字（与上面相同）
# 5.2.5 检查多个条件
# and 和 or 的使用
# 5.2.6 检查特定值是否包含在列表中
# in 的使用
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) #True
# 5.2.7 检查特定值是否不包含在列表中
# not in 的使用
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' not in requested_toppings) #False
#5.2.8 布尔表达式
# 随着你对编程的了解越来越深入，将遇到术语布尔表达式，它不过是条件测试的别名。与条件表达式一样，布尔表达式的结果要么为True，要么为False。
game_active = True

# 5.3 if语句
# 5.3.1 简单的if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")
# 5.3.2 if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
# 5.3.3 if-elif-else结构
age = 12
if age < 4:
    print("Your admission cost is $0．")
elif age < 18:
    print("Your admission cost is $5．")
else:
    print("Your admission cost is $10．")
# 5.3.4 使用多个elif代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# 5.3.5 省略else代码块
# Python并不要求if-elif结构后面必须有else代码块。在有些情况下，else代码块很有用；而在其他一些情况下，使用一条elif语句来处理特定的情形更清晰：
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# 5.3.6 测试多个条件
# 多个条件块儿不要写在一起而已。。。。

# 5.4 使用if语句处理列表
# 5.4.1 检查特殊元素
# 5.4.2 确定列表不是空的，如果列表为空返回False，反之True。
# 5.4.3 使用多个列表
