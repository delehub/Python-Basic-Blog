'''
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

dict = {key1 : value1, key2 : value2 }

'''

'''
info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
说明：

字典和列表一样，也能够存储多个数据
列表中找某个元素时，是根据下标进行的
字典中找某个元素时，是根据'名字'（就是冒号:前面的那个值，例如上面代码中的'name'、'id'、'sex'）
字典的每个元素由2部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值
'''

infodict = {'name':'张三', 'id':100, 'sex':'m', 'address':'中国北京','age':'20','born':'1999','score':'666'}

# 访问键值

print(infodict['name'])
print(infodict['id'])
print(infodict['address'])
print(infodict['sex'])
print(infodict['score'])
print(infodict['age'])
print(infodict['born'])

'''
张三
100
中国北京
m
666
20
1999
'''

# 若访问不存在的键，则会报错
# print(infodict['ages'])

'''
报错：
Traceback (most recent call last):
  File "e:/Basic/dict.py", line 33, in <module>
    print(infodict['ages'])
KeyError: 'ages'
'''

# 不确定字典中是否存在某个键而又想获取其值时，可以使用get方法，还可以设置默认值

ages = infodict.get('ages')
Type = type(ages)
print(Type)
# <class 'NoneType'>
ages = infodict.get('ages',112233) # 若infodict中不存在'ages'这个键，就返回默认值112233

print('ages=',ages) # ages= 112233

# 常见操作
'''
1.查看字典元素
'''
# key 键值搜索
print(infodict['name'])
# get 请求 
print(infodict.get('id'))  # 存在id 搜索键值
print(infodict.get('idd')) # 不存在idd 返回 None

'''
2.修改字典元素
'''
info = {'name':'张三', 'id':100, 'sex':'m', 'address':'中国北京','age':'20','born':'1999','score':'666'}

newId = input('请输入新的学号:')
info['id'] = int(newId)

print('修改之后的id为%d:'%info['id'])

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
dict1['Age'] = 8               # 更新 Age
dict1['School'] = "菜鸟教程"  # 添加信息
 
 
print ("dict['Age']: ", dict1['Age'])
print ("dict['School']: ", dict1['School'])

'''
请输入新的学号:666
修改之后的id为666:
'''

'''
3.添加元素
'''
infoadd = {'name':'班长', 'sex':'f', 'address':'中国北京'}

# print('id为:%d'%info['id'])#程序会终端运行，因为访问了不存在的键

newborn= input('请输入新的学号')

infoadd['newborn'] = newborn

print('添加之后的newborn为:%s'%infoadd['newborn']) #  %s 字符串


'''
4.删除元素
'''
infodel = {'name':'张三', 'id':100, 'sex':'m', 'address':'中国北京','age':'20','born':'1999','score':'666'}

print('删除前,%s'%infodel['name'])
print('删除前,%s'%infodel)
# del infodel['name']
# del infodel

print('删除后,%s'%infodel)
# print('删除后,%s'%infodel['name']


# del infodel['name'] 删除后不；能访问 报错
# del infodel  name 'infodel' is not defined   不存在
'''
删除前,张三
删除前,{'name': '张三', 'id': 100, 'sex': 'm', 'address': '中国北京', 'age': '20', 'born': '1999', 'score': '666'}
Traceback (most recent call last):
  File "e:/Basic/dict.py", line 121, in <module>
    print('删除后,%s'%infodel)
NameError: name 'infodel' is not defined
'''    
infoclear = {'name':'张三', 'id':100, 'sex':'m', 'address':'中国北京','age':'20','born':'1999','score':'666'}
print('clear 清除之前：',infoclear)
infoclear.clear()
print('clear 清除之后：',infoclear)

'''
clear 清除之前： {'name': '张三', 'id': 100, 'sex': 'm', 'address': '中国北京', 'age': '20', 'born': '1999', 'score': '666'}
clear 清除之后： {}
'''

# 字典键特性 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 
'''
字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

实例
#!/usr/bin/python3
 
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
 
print("dict['Name']: ", dict['Name'])
以上实例输出结果：

dict['Name']:  小菜鸟
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

实例
#!/usr/bin/python3
 
dict = {['Name']: 'Runoob', 'Age': 7}
 
print("dict['Name']: ", dict['Name'])
以上实例输出结果：

Traceback (most recent call last):
  File "test.py", line 3, in <module>
    dict = {['Name']: 'Runoob', 'Age': 7}
TypeError: unhashable type: 'list'
'''

# len 
infolen = {'name':'张三', 'id':100, 'sex':'m', 'address':'中国北京','age':'20','born':'1999','score':'666'}
print('字典元素(键)个数：',len(infolen))
# 字典元素(键)个数： 7

# str(dict) 输出字典，以可打印的字符串表示。
dict_to_str = str(infolen)
print(dict_to_str)

# dict内置方法

# dict内置方法

'''
dict.clear() 删除
'''
dictclear = {'name':'张三', 'id':100, 'sex':'m', 'address':'中国北京','age':'20','born':'1999','score':'666'}

print ("字典长度 : %d" %  len(dictclear))
dictclear.clear()
print ("字典删除后长度 : %d" %  len(dictclear))

"""
字典长度 : 7
字典删除后长度 : 0
"""
# len 计算字典长度
dictclen = {'name':'张三', 'id':100, 'sex':'m', 'address':'中国北京','age':'20','born':'1999','score':'666'}
dict_len =  len(dictclen)
print(dict_len)

# keys 返回一个包含字典所有KEY(键)的列表

dictkey = dictclen
dict_key = dictkey.keys()
print(dict_key)

# values 返回一个包含字典所有values(键值)的列表
dictvalues = dictkey
dict_values = dictvalues.values()
print(dict_values)

# items  返回一个包含所有（键，值）元祖的列表

dictitems = dictkey
dict_items = dictitems.items()
print(dict_items)

# has_key dict.has_key(key)如果key在字典中，返回True，否则返回False
# python3 删除了

# dict_has_key = dictkey
# dict_haskey_name = dict_has_key.has_key('name')
# # dict_haskey_other = dict_has_key.has_key('other')
# print(dict_haskey_name)


'''
dict_keys(['name', 'id', 'sex', 'address', 'age', 'born', 'score'])
dict_values(['张三', 100, 'm', '中国北京', '20', '1999', '666'])
dict_items([('name', '张三'), ('id', 100), ('sex', 'm'), ('address', '中国北京'), ('age', '20'), ('born', '1999'), ('score', '666')])
'''



'''
dict.copy()
函数返回一个字典的浅复制。
'''
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)

'''
新复制的字典为 :  {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
'''

'''
fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。

dict.fromkeys(seq[, value])

seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。

返回值
该方法返回一个新字典。
'''



#encoding=utf-8

import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)    
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)

'''
# 练习题
x = True
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('china')

print(len(country_counter))

# 3

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)

# 4

'''