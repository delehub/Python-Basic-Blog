'''

序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

Python有6个序列的内置类型，但最常见的是列表和元组。

序列都可以进行的操作包括索引，切片，加，乘，检查成员。

此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型

'''

# list 
'''
变量A的类型为列表
    namesList = ['xiaoWang','xiaoZhang','xiaoHua']

比C语言的数组强大的地方在于列表中的元素可以是不同类型的
    testList = [1, 'a']

序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推.
'''
# demo

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

print('第一个列表：')
for i in range(0,4):
    print(list1[i],end='')

print('第二个列表：')
for i in range(0,7):
    print(list2[i])

'''
list1[0]:  Google
list2[1:5]:  [2, 3, 4, 5]
第一个列表：
GoogleRunoob19972000第二个列表：
1234567
'''

# 更新列表
list3 = ['python', 'COVID-19', 2003, 2020,'deeplearning']
print ("原始列表 : ", list3) 
print("第三个元素为 : ", list3[2])
list3[2] = 2001
print("更新后的第三个元素为 : ", list3[2])
print("更新列表 : ", list3)

# 删除列表元素
list4 = ['python', 'COVID-19', 2003, 2020,'deeplearning','Ai']
 
print ("原始列表 : ", list4)
del list4[3]
print("删除第三个元素 : ", list4)

'''
结果：

# 更新列表

原始列表 :  ['python', 'COVID-19', 2003, 2020, 'deeplearning']
第三个元素为 :  2003
更新后的第三个元素为 :  2001
更新列表 :  ['python', 'COVID-19', 2001, 2020, 'deeplearning']

# 删除列表元素

原始列表 :  ['python', 'COVID-19', 2003, 2020, 'deeplearning', 'Ai']
删除第三个元素 :  ['python', 'COVID-19', 2003, 'deeplearning', 'Ai']
'''

'''
列表的循环遍历
'''

# for 循环 # 更加简单
print('for 循环遍历')
namesList = ['xiaoWang','xiaoZhang','xiaoHua']
for name in namesList:
    print(name)

# while 循环
'''
1. 列表的初始化
2. 计算列表长度(元素个数)
3. while 循环 if 判断(循环次数与列表的length大小比较)
'''
print('while 循环遍历')
pythonList = ['python', 'COVID-19', 2003, 2020, 'deeplearning', 'Ai']

length = len(pythonList)

listnum= 0

while listnum<length:
    print(pythonList[listnum])
    listnum+=1

'''
结果：

    for 循环遍历

    xiaoWang
    xiaoZhang
    xiaoHua

    while 循环遍历

    python
    COVID-19
    2003
    2020
    deeplearning
    Ai
'''

'''
Python列表脚本操作符

'''

# len
listtest = [1999,2003,'python', 'COVID-19','deeplearning', 'Ai','baidu-ai',2020]
lennum = len(listtest)
print(lennum)
# 组合
litstest1 = [1999,2003,2020,2035]
listtest2 = ['python', 'COVID-19','deeplearning', 'Ai','baidu-ai']
listand = litstest1 + listtest2
print(listand)
# 重复
litstest3 = [1999,2003,2020,2035,'baidu-ai']
litstest4 = (litstest3)*4
print(litstest4)

# 判断元素是否在列表之中
litstest3 = [1999,2003,2020,2035,'baidu-ai']

if (2020 in litstest3):
    print('yes')
else:
    print('no')

# 迭代
litstest5 = [1999,2003,2020,2035,'baidu-ai']
for num in litstest5:
    print(num) # end = "" 双引号的内容可以自行添加

'''
结果：
8
[1999, 2003, 2020, 2035, 'python', 'COVID-19', 'deeplearning', 'Ai', 'baidu-ai']
[1999, 2003, 2020, 2035, 'baidu-ai', 1999, 2003, 2020, 2035, 'baidu-ai', 1999, 2003, 2020, 2035, 'baidu-ai', 1999, 2003, 2020, 2035, 'baidu-ai']
yes
1999
2003
2020
2035
baidu-ai
'''


'''
Python列表截取与拼接
'''
listtest6 = [1999,2003,'python', 'COVID-19','deeplearning', 'Ai','baidu-ai',2020]
 # 前开后闭
print(listtest6[2:6])
print(listtest6[:-2])
print(listtest6[1:])

'''
结果：
['python', 'COVID-19', 'deeplearning', 'Ai']
[1999, 2003, 'python', 'COVID-19', 'deeplearning', 'Ai']
[2003, 'python', 'COVID-19', 'deeplearning', 'Ai', 'baidu-ai', 2020]
'''

# 嵌套列表

x = ['a','b','c','d']
y = [1,2,3,4]
z = [x,y]
print(x)
print(y)
print(z)
"""
['a', 'b', 'c', 'd']
[1, 2, 3, 4]
[['a', 'b', 'c', 'd'], [1, 2, 3, 4]]
"""
