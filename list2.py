# 列表的基本操作

'''

append() 方法用于在列表末尾添加新的对象。

list.append(obj)

参数

obj：-这是要添加到列表中的对象。

返回值

此方法不返回任何值，但更新现有列表

'''


# A = ['xiaoWang','xiaoZhang','xiaoHua']

# print("-----添加之前，列表A的数据-----")
# for tempName in A:
#     print(tempName)

# #提示、并添加元素
# temp = input('请输入要添加的学生姓名:')
# A.append(temp)


# print("-----添加之后，列表A的数据-----")
# for tempName in A:
#     print(tempName)


'''
描述
count() 方法用于统计某个元素在列表中出现的次数。

list.count(obj)

参数
obj -- 列表中统计的对象。

返回值
返回元素在列表中出现的次数。

'''

list1 = ['app','123',123,'App','python','123']

mylistcount=list1.count('123') # "123 查找的对象" 
print(mylistcount) # 打印查找的对象的次数多少

# 统计某个元素在列表中出现的次数

'''
extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
'''

# 列表
language = ['French', 'English', 'German',2020,1999]
print(language)

# 元组 
'''
Python 的元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号，列表使用方括号。

元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可)
'''

# 添加元组元素到列表末尾
language_tuple = ('Spanish', 'Portuguese','JAVA','Python')
print(language_tuple)
language.extend(language_tuple)
print('新列表1: ', language)


# 集合 (set是一个无序的不重复元素序列)
language_set = {'Chinese', 'Japanese','Android','deeplearning'}
print(language_set)
# 添加集合元素到列表末尾
language.extend(language_set)
print('新列表2: ', language)

'''
结果：
['French', 'English', 'German', 2020, 1999]
('Spanish', 'Portuguese', 'JAVA', 'Python')
新列表1:  ['French', 'English', 'German', 2020, 1999, 'Spanish', 'Portuguese', 'JAVA', 'Python']
{'deeplearning', 'Chinese', 'Japanese', 'Android'}
新列表2:  ['French', 'English', 'German', 2020, 1999, 'Spanish', 'Portuguese', 'JAVA', 'Python', 'deeplearning', 'Chinese', 'Japanese', 'Android']
'''

'''
index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

list.index(x[, start[, end]])

x-- 查找的对象。
start-- 可选，查找的起始位置。
end-- 可选，查找的结束位置。

返回值

该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
'''
listindex = ['java','python','android','vue','wechat','C#','C++']
print ('python 索引值为', listindex.index('python'))
print ('C++ 索引值为', listindex.index('C++'))

'''
python 索引值为 1
C++ 索引值为 6
'''

'''
insert() 函数用于将指定对象插入列表的指定位置。

list.insert(index, obj)

参数
index -- 对象obj需要插入的索引位置。
obj -- 要插入列表中的对象。

返回值
该方法没有返回值，但会在列表指定位置插入对象。
'''

# insert("位置","插入对象")
listinsert = ['java','python','android','vue','wechat','C#','C++']
listinsert.insert(1, 'Baidu')
listinsert.insert(2,'paddlepaddle')
print ('列表插入元素后为 : ', listinsert)

'''
结果：
列表插入元素后为 :  ['java', 'Baidu', 'paddlepaddle', 'python', 'android', 'vue', 'wechat', 'C#', 'C++']
['paddlepaddle', 'java', 'python', 'android', 'vue', 'wechat', 'C#', 'C++']
'''

'''
pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

list.pop([index=-1])
参数

index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。

列表从左往右0--》
列表从右往左《-- -1
返回值

该方法返回从列表中移除的元素对象
'''
listpop = ['paddlepaddle','java','python','android','vue','wechat','C#','C++'] # (-8)《-- (-1)
print(listpop)
listpop_1 = listpop.pop(-2)
listpop_2 = listpop.pop(-3)
print(listpop_1)
print(listpop_2)
print(listpop)
'''
结果：
C#
vue
['paddlepaddle', 'java', 'python', 'android', 'wechat', 'C++']

'''

'''
remove() 函数用于移除列表中某个值的第一个匹配项。

list.remove(obj)

obj -- 列表中要移除的对象。

返回值
该方法没有返回值但是会移除列表中的某个值的第一个匹配项。
'''

listremove = ['remove','paddlepaddle','java','python','android','vue','wechat','C#','C++']
print(listremove)
listremove.remove('vue')
listremove1 = listremove
print(listremove1)

'''
结果：
['remove', 'paddlepaddle', 'java', 'python', 'android', 'vue', 'wechat', 'C#', 'C++']
['remove', 'paddlepaddle', 'java', 'python', 'android', 'wechat', 'C#', 'C++']
'''

'''
reverse() 函数用于反向列表中元素。

list.reverse()

返回值
该方法没有返回值，但是会对列表的元素进行反向排序。
'''
print('listreverse 测试')
listreverse = ['reverse','paddlepaddle','java','python','android','vue','wechat','C#','C++']
print(listreverse)
listreverse.reverse()
print(listreverse)

'''
结果：
['reverse', 'paddlepaddle', 'java', 'python', 'android', 'vue', 'wechat', 'C#', 'C++']
['C++', 'C#', 'wechat', 'vue', 'android', 'python', 'java', 'paddlepaddle', 'reverse']
'''

'''
sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。

list.sort( key=None, reverse=False)

key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。

返回值
该方法没有返回值，但是会对列表的对象进行排序
'''

list_sort = ['sort','paddlepaddle','java','python','android','vue','wechat','C#','C++']
print('排序前：',list_sort)
# 降序  
list_sort.sort(reverse=True)
print('降序排序后',list_sort)

# 升序
list_sort.sort()
print('升序排序后',list_sort)


number_sort = [1,2,3,11,5,6,7,99]
print('数字排序前：',number_sort)

# 降序  
number_sort.sort(reverse=True)
print('数字排序后：',number_sort)

number_sort.sort()
print('数字排序后：',number_sort)
'''
按照字母的排序a-->z
排序前：   ['sort', 'paddlepaddle', 'java', 'python', 'android', 'vue', 'wechat', 'C#', 'C++']
降序排序后 ['wechat', 'vue', 'sort', 'python', 'paddlepaddle', 'java', 'android', 'C++', 'C#']
升序排序后 ['C#', 'C++', 'android', 'java', 'paddlepaddle', 'python', 'sort', 'vue', 'wechat']
'''
'''
数字排序前： [1, 2, 3, 11, 5, 6, 7, 99]
数字排序后： [99, 11, 7, 6, 5, 3, 2, 1]
数字排序后： [1, 2, 3, 5, 6, 7, 11, 99]
'''

'''
list.clear()
clear() 函数用于清空列表，类似于 del a[:]
'''

list_clear = ['sort','paddlepaddle','java','python','android','vue','wechat','C#','C++']
print('清除前',list_clear)
list_clear.clear()
print('清除后',list_clear)

'''
清除前 ['sort', 'paddlepaddle', 'java', 'python', 'android', 'vue', 'wechat', 'C#', 'C++']
清除后 []
'''

'''
copy() 函数用于复制列表
list.copy()
'''

list_copy1 = ['copy','paddlepaddle','java','python','android','vue','wechat','C#','C++']
list_copy2 = []
print(list_copy2)
list_copy2 = list_copy1.copy()
print(list_copy2)

'''
[]
['copy', 'paddlepaddle', 'java', 'python', 'android', 'vue', 'wechat', 'C#', 'C++']
'''