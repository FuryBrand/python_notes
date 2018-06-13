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

