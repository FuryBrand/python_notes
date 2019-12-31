# 用户输入与while循环
# 7.1 函数input()的工作原理
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# 7.1.1 编写清晰的程序
# tips-1：通过在提示末尾（这里是冒号后面）包含一个空格，可将提示与用户输入分开，让用户清楚地知道其输入始于何处。
# tips-2：提示可能超过一行，例如，你可能需要指出获取特定输入的原因。在这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input()。这样，即便提示超过一行，input()语句也非常清晰。
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
# 7.1.2 使用int()来获取数值输入
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
# 7.1.3 求模运算符
# 处理数值信息时，求模运算符（%）是一个很有用的工具，它将两个数相除并返回余数。可用于判断奇偶。
if height % 2 == 0:
    print("\nThe number " + str(height) + " is even.")
# 7.1.4 在Python 2.7中获取输入
# 如果你使用的是Python 2.7，应使用函数raw_input()来提示用户输入。这个函数与Python 3中的input()一样，也将输入解读为字符串。
# Python 2.7也包含函数input()，但它将用户输入解读为Python代码，并尝试运行它们。
# 7.2 while循环简介
# 7.2.1 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 7.2.2 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
# 7.2.3 使用标示
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
# 7.2.4 使用break退出循环（适用于while和for）
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        break
# 7.2.5 在循环中使用continue
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句。
# 只打印奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# 7.2.6 避免无限循环
# 7.3 使用while循环来处理列表和字典
# for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。
# 7.3.1 在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# 7.3.2 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] #['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets) #['dog', 'dog', 'goldfish', 'rabbit']
# 7.3.3 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
