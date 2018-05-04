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



