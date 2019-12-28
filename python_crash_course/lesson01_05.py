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

#5.3 if语句
# 5.3.1 简单的if语句