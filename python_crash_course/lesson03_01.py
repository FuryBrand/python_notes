"""
列表由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0～9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。 
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

#使用列表中的值来
message = "My first bicyle was a "+bicycles[0].title()+"."
print(message)#My first bicyle was a Trek.