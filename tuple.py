''' 元组tuple
特性：
　　1.可存放多个值
　　2.不可变
　　3.按照从左到右的顺序定义元组元素，下标从0开始顺序访问，有序.
'''
# 类型 
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"   #  不需要括号也可以
mylist = [1,'2020','python']
mystr = 'python-learn'
print(type(tup1))
print(type(tup2))
print(type(tup3))
print(type(mylist))
print(type(mystr))


'''
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'list'>
<class 'str'>
'''

'''
注意 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
'''
tup4 = (12) # int类型 # 不加逗号，类型为整型
tup5 = (12,) # 元组类型 # 加上逗号，类型为元组
 
print(type(tup4))
print(type(tup5))

'''
<class 'int'>
<class 'tuple'>
'''

'''
访问元组成员

'''
tup6 = ('Google', 'Runoob', 1997, 2000)
tup7 = (1, 2, 3, 4, 5, 6, 7 )
 
print ("tup1[0]: ", tup6[0])
print ("tup2[1:5]: ", tup7[1:5])

'''
tup1[0]:  Google
tup2[1:5]:  (2, 3, 4, 5)
'''

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

mytup1 = (12, 34.56)
mytup2 = ('python', 'deep')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
mytup3 = mytup1 + mytup2
print(mytup3)

# (12, 34.56, 'python', 'deep')

'''
删除元组
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
'''

tup = ('Google', 'Youtube','Python',1999, 2020)
 
print (tup)
del tup
# print ("删除后的元组 tup : ")
# print (tup)


'''
('Google', 'Youtube', 'Python', 1999, 2020)
# 报错
删除后的元组 tup :
Traceback (most recent call last):
  File "e:/Basic/tuple.py", line 84, in <module>
    print (tup)
NameError: name 'tup' is not defined
'''

'''
元组运算符
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组
'''
x_tuple = ('Google', 'Youtube','Python',1999, 2020)
y_tuple = ('java','Vscode',1993,'helloworld')
# len 计算元组成员个数
x_tuplelen = len(x_tuple)
y_tuplelen = len(y_tuple)
# 合并 元组
z_tuple = x_tuple + y_tuple
# 复制 元组
copy_tuple = (x_tuple)*3
copy_tuplelen = len(copy_tuple)
# 元素是否存在

if (2020 in x_tuple):
    print('yes')
else:
    print('no')
# 结果 yes
if ('2020' in x_tuple):
    print('yes')
else:
    print('no')
# 结果 no

print('x_tuple元组成员个数：',x_tuplelen)
print('y_tuple元组成员个数：',y_tuplelen)
print('x_tuple y_tuple 连接合并',z_tuple)
print('复制结果',copy_tuple)
'''
x_tuple元组成员个数： 5
y_tuple元组成员个数： 4
x_tuple y_tuple 连接合并 ('Google', 'Youtube', 'Python', 1999, 2020, 'java', 'Vscode', 1993, 'helloworld')
复制结果 ('Google', 'Youtube', 'Python', 1999, 2020, 'Google', 'Youtube', 'Python', 1999, 2020, 'Google', 'Youtube', 'Python', 1999, 2020) 
'''

# 迭代  (循环遍历打印)
Mytuple = ('Google', 'Youtube','Python',1999,2003,'COVID-19','deeplearning', 'Ai','baidu-ai',2020)
for i in Mytuple:
    print(i)

'''
Google
Youtube
Python
1999
2003
COVID-19
deeplearning
Ai
baidu-ai
2020
'''

'''
元组索引，截取
因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，
'''

Mytuple = ('Google', 'Youtube','Python',1999,2003,'COVID-19','deeplearning', 'Ai','baidu-ai',2020)
print(Mytuple[::-1]) # 反向
print(Mytuple[2::])  # 从第3个打印
print(Mytuple[0::2]) # 从0开始 每隔2个打印
print(Mytuple[-2])   # 打印倒数第二个成员信息
print(Mytuple[2])

'''
结果：
(2020, 'baidu-ai', 'Ai', 'deeplearning', 'COVID-19', 2003, 1999, 'Python', 'Youtube', 'Google')
('Python', 1999, 2003, 'COVID-19', 'deeplearning', 'Ai', 'baidu-ai', 2020)
('Google', 'Python', 2003, 'deeplearning', 'baidu-ai')
baidu-ai
Python
'''

'''
元组内置基本操作函数
'''
# len 计算成员个数
f_tuple = (1999,2000,2003,2008,2009,2012,2018,2019,2020)
f_tuple_len = len(f_tuple)
print('f-tuple 成员个数：',f_tuple_len)
# max
f_tuple_max = max(f_tuple)
print('f-tuple 成员max：',f_tuple_max)
# min
f_tuple_min = min(f_tuple)
print('f-tuple 成员main：',f_tuple_min)

'''
结果：
f-tuple 成员个数： 9
f-tuple 成员max： 2020
f-tuple 成员main： 1999
'''

# tuple(iterable) 将可迭代系列转换为元组

Mylist = [1999,2003,'python', 'COVID-19','deeplearning', 'Ai','baidu-ai',2020,'list to tuple']
print('Mylist:',Mylist)
list_to_tuple = tuple(Mylist)
print('Mylist 转换成 Tuple :',list_to_tuple)

'''
结果：
Mylist: [1999, 2003, 'python', 'COVID-19', 'deeplearning', 'Ai', 'baidu-ai', 2020, 'list to tuple']
Mylist 转换成 Tuple : (1999, 2003, 'python', 'COVID-19', 'deeplearning', 'Ai', 'baidu-ai', 2020, 'list to tuple')
'''