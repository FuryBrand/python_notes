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
# 5.4.3 使用多个列表（for和if的嵌套，没啥）


# 5.5 设置if语句的格式
# PEP 8提供的唯一建议是，在诸如==、>=和<=等比较运算符两边各添加一个空格，例如，if age < 4:要比if age<4:好。
# 这样的空格不会影响Python对代码的解读，而只是让代码阅读起来更容易。

# 5.6 小结

# 6.0 字典
# 6.1 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) #green
print(alien_0['points']) #5
# 6.2 使用字典
# 在Python中，字典是一系列键—值对，没有存储限制。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
# 6.2.1 访问字典中的值
# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键（可以看6.1的示例）
# 6.2.2 添加键——值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0) #{'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) #{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
# 6.2.3 先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0) #{'color': 'green', 'points': 5}
# 使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常都需要先定义一个空字典。
# 6.2.4 修改字典中的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".") #The alien is green.
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".") #The alien is now yellow.
# 6.2.5 删除键——值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0) #{'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0) #{'color': 'green'}
# 6.2.6 由类似对象组成的字典
# 注意字典的换行和print的换行写法。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".") #Sarah's favorite language is C.
# 6.3 遍历字典.items()
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
for key, value in user_0.items():
    print('Key:' + key + ', value:' + value) #Key:username, value:efermi /n Key:first, value:enrico /n Key:last, value:fermi
# 注意：即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。
# 6.3.2 遍历字典中的所有建.keys()该方法返回的是一个列表。不写的话，默认也是遍历key。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title()) #Jen Sarah Phil Edward
for name in favorite_languages:
    print(name.title()) #Jen Sarah Phil Edward
# 6.3.3 按顺序遍历字典中的所有键
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
# 6.3.4 遍历字典中的所有值
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for language in sorted(favorite_languages.values()):
    print(language.title())
# 用set()来过滤相同的值，set返回一个集合，集合类似于列表但是没有重复项
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for language in set(favorite_languages.values()):
    print("use set(): " + language.title())

# 6.4 嵌套
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。