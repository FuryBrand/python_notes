"""
列表简介及操作列表、元组、PEP8规范
"""
"""
列表简介：列表由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0～9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。 
在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。 
"""
#定义列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) #['trek', 'cannondale', 'redline', 'specialized']
#访问列表元素，索引是从0开始的
print(bicycles[0]) #trek
#结合字符串方法，让输出的首字母大写
print(bicycles[0].title()) #Trek
#利用负数索引来从后向前访问元素，-1是最后一个元素
print(bicycles[-1])#specialized
print(bicycles[-2])#redline
#使用列表中的值
message = "My first bicyle was a "+bicycles[0].title()+"."
print(message)#My first bicyle was a Trek.

#3.2 修改、添加和删除元素
#修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)#['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)#['ducati', 'yamaha', 'suzuki']
#利用append方法在列表末尾添加元素
motorcycles.append('Xiaoniao')
print(motorcycles)#['ducati', 'yamaha', 'suzuki', 'Xiaoniao']
#创建空列表
bikes = []
print(bikes)#[]
#利用insert方法在列表的任意位置插入新元素
motorcycles.insert(0,'honda')
print(motorcycles)#['honda', 'ducati', 'yamaha', 'suzuki', 'Xiaoniao']
#使用del语句从列表中删除元素
del motorcycles[-1]
print(motorcycles)#['honda', 'ducati', 'yamaha', 'suzuki']
#使用pop方法获取队尾的的元素，并删除他
popped_motorcyle = motorcycles.pop()
print(motorcycles)#['honda', 'ducati', 'yamaha']
print(popped_motorcyle)#suzuki
#使用pop方法获取任意位置的元素，并删除他
second_motorcyle = motorcycles.pop(1)
print(motorcycles)#['honda', 'yamaha']
print(second_motorcyle)#ducati
#利用remove方法根据值删除元素
motorcycles.remove('yamaha')
print(motorcycles)#['honda']

#3.3 组织列表
# 使用sort方法对列表进行永久性排序(正序)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)#['audi', 'bmw', 'subaru', 'toyota']
# 使用sort(reverse=True)方法对列表进行永久性排序(倒序)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)#['toyota', 'subaru', 'bmw', 'audi']
# 使用sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars)) #['audi', 'bmw', 'subaru', 'toyota']
print(cars) #['bmw', 'audi', 'toyota', 'subaru']
# 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars) #['subaru', 'toyota', 'audi', 'bmw']
# 确定列表的长度
cars = ['subaru', 'toyota', 'audi', 'bmw']
print(len(cars)) #4

"""
操作列表，如何轻松遍历列表
"""
# 4.1 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + '.\n') #默认换行，然后通过.\n额外换行

# 4.3 创建数值列表
# 4.3.1 使用函数range() 可以生成一系列数字
for value in range(1,5):
    print(value) # 打印1-4
# 4.3.2 使用range()创建数字列表
numbers = list(range(1,6))
print(numbers) #[1, 2, 3, 4, 5]
even_numbers = list(range(2,11,2)) #range()可以指定间隔
print(even_numbers) #[2, 4, 6, 8, 10]
# 4.3.3 对数字列表执行简单的统计计算
# 专门处理数字列表的Python函数。
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) #0
print(max(digits)) #9
print(sum(digits)) #45
# 4.3.4 列表解析，将for循环和创建新元素的代码合并成一行，并自动附加新元素。
squares = [value**2 for value in range(1,11)]
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 4.4使用列表的一部分
# 4.4.1切片，切之后还是一个list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4]) #['martina', 'michael', 'florence']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) #['charles', 'martina', 'michael', 'florence']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) #['michael', 'florence', 'eli']
# 4.4.2 遍历切片
# 4.4.3 复制列表，需利用切片来复制列表，不然指向的是同一列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #my_foods和friend_foods是两个独立的列表了

# 4.5 元组
# Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
# 4.5.1 定义元组
dimensions = (200, 50)
print(dimensions[0]) #200
print(dimensions[1]) #50
# 4.5.2 遍历元组中的所有值（与list一致）
# 4.5.3 修改元组变量，虽然不能修改元组的元素，但可以给存储元组的变量赋值。说白了就是赋个新的值。

# 4.6 设置代码格式
# 4.6.1 格式设置指南
"""
若要提出Python语言修改建议，需要编写Python改进提案（Python Enhancement Proposal，PEP）。PEP 8是最古老的PEP之一，它向Python程序员提供了代码格式设置指南。PEP 8的篇幅很长，但大都与复杂的编码结构相关。
如果一定要在让代码易于编写和易于阅读之间做出选择，Python程序员几乎总是会选择后者。下面的指南可帮助你从一开始就编写出清晰的代码。
"""
# 4.6.2 缩进
"""
PEP 8建议每级缩进都使用四个空格，这既可提高可读性，又留下了足够的多级缩进空间。
在字处理文档中，大家常常使用制表符而不是空格来缩进。对于字处理文档来说，这样做的效果很好，但混合使用制表符和空格会让Python解释器感到迷惑。每款文本编辑器都提供了一种设置，可将输入的制表符转换为指定数量的空格。你在编写代码时应该使用制表符键，但一定要对编辑器进行设置，使其在文档中插入空格而不是制表符。在程序中混合使用制表符和空格可能导致极难解决的问题。如果你混合使用了制表符和空格，可将文件中所有的制表符转换为空格，大多数编辑器都提供了这样的功能。
"""
# 4.6.3 行长
"""
很多Python程序员都建议每行不超过80字符。最初制定这样的指南时，在大多数计算机中，终端窗口每行只能容纳79字符；当前，计算机屏幕每行可容纳的字符数多得多，为何还要使用79字符的标准行长呢？这里有别的原因。专业程序员通常会在同一个屏幕上打开多个文件，使用标准行长可以让他们在屏幕上并排打开两三个文件时能同时看到各个文件的完整行。PEP 8还建议注释的行长都不超过72字符，因为有些工具为大型项目自动生成文档时，会在每行注释开头添加格式化字符。
PEP 8中有关行长的指南并非不可逾越的红线，有些小组将最大行长设置为99字符。在学习期间，你不用过多地考虑代码的行长，但别忘了，协作编写程序时，大家几乎都遵守PEP 8指南。在大多数编辑器中，都可设置一个视觉标志——通常是一条竖线，让你知道不能越过的界线在什么地方。
"""
# 4.6.5 空行
"""
要将程序的不同部分分开，可使用空行。你应该使用空行来组织程序文件，但也不能滥用；只要按本书的示例展示的那样做，就能掌握其中的平衡。例如，如果你有5行创建列表的代码，还有3行处理该列表的代码，那么用一个空行将这两部分隔开是合适的。然而，你不应使用三四个空行将它们隔开。
空行不会影响代码的运行，但会影响代码的可读性。Python解释器根据水平缩进情况来解读代码，但不关心垂直间距。
"""
# 4.6.5 其他格式设置指南
"""
PEP 8：请访问https://python.org/dev/peps/pep-0008/，阅读PEP 8格式设置指南。当前，这些指南适用的不多，但你可以大致浏览一下。
"""