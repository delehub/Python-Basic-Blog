'''
集合跟我们学的列表有点像，也是可以存一堆数据，不过它有几个独特的特点，令其在整个Python语言中占有一席之地，


1. 集合里面的元素不可变，代表你不能存一个list、dict 在集合里，字符串、数字、元组等不可变类型可以存

2. 集合天生去重，在集合里没办法存重复的元素

3. 集合无序，不像列表一样通过索引来标记在列表中的位置 ，元素是无序的，集合中的元素没有先后之分，如集合{3,4,5}和{3,5,4}算作同一个集合
'''
# 创建集合set
set_a = {1,2,3,4,2,'alex',3,'rain','alex'}

print('set_a集合元素：',set_a)

# set_a集合元素： {1, 2, 3, 4, 'alex', 'rain'}

# 列表去重创建集合

list_set = [1,2,3020,4,2,'alex',3,'rain','alex','python']
print('列表list_set:',list_set)
list_to_set = set(list_set)

print('list_to_set:',list_to_set)

list_set_to = list(set(list_to_set))

print('list_set_to:',list_set_to)
'''
列表list_set: [1, 2, 3020, 4, 2, 'alex', 3, 'rain', 'alex', 'python']
list_to_set: {1, 2, 3, 'alex', 4, 3020, 'rain', 'python'}
list_set_to: [1, 2, 3, 4, 'rain', 'python', 3020, 'alex']
'''


s_1024 = {"佩奇","老男孩","海峰","马JJ","老村长","黑姑娘","Alex"}
s_pornhub = {"Alex","Egon","Rain","马JJ","Nick","Jack"}
print(s_1024 & s_pornhub)  # 交集, elements in both set
print(s_1024 | s_pornhub)  # 并集 or 合集
print(s_1024 - s_pornhub)  # 差集 , only in 1024
print(s_pornhub - s_1024)  # 差集,  only in pornhub
print(s_1024 ^ s_pornhub)  # 对称差集, 把脚踩2只船的人T出去

'''
两个集合之间一般有三种关系，相交、包含、不相交。在Python中分别用下面的方法判断：
'''

print(s_1024.isdisjoint(s_pornhub))     # 判断2个集合是不是不相交，返回True or False
print(s_1024.issubset(s_pornhub))       # 判断s_1024是不是s_pornhub的子集，返回True or False
print(s_1024.issuperset(s_pornhub))     # 判断s_1024是不是s_pornhub的父集，返回True or False

"""
{'马JJ', 'Alex'}
{'Nick', '老男孩', '马JJ', '佩奇', '老村长', 'Rain', '黑姑娘', 'Jack', 'Egon', '海峰', 'Alex'}
{'老男孩', '佩奇', '老村长', '黑姑娘', '海峰'}
{'Nick', 'Egon', 'Rain', 'Jack'}
{'老村长', 'Rain', 'Nick', '老男孩', '佩奇', '黑姑娘', 'Jack', 'Egon', '海峰'}
False
False
False
"""

# add
set_f1 = {1, 2, 3020, 4, 2, 'alex', 3, 'rain', 'alex', 'python'}
print('set_f1:',set_f1)
set_f1.add('Youtube')
print('set_f_add:',set_f1)

'''
set_f: {'alex', 1, 2, 4, 3, 'python', 3020, 'rain'}
set_f_add: {'alex', 1, 2, 4, 3, 'python', 3020, 'Youtube', 'rain'}
'''

set_f2 = {1, 2, 3020, 4, 22, 'alex', 3, 'rain', 'alex', 'python'}
print('set_f2:',set_f2)
set_f2.remove(2)
print('set_f_remove:',set_f2)

'''
set_f2: {1, 2, 3, 4, 3020, 'rain', 'alex', 'python', 22}
set_f_remove: {1, 3, 4, 3020, 'rain', 'alex', 'python', 22}
'''
# len 计算集合 元素个数
set_f3 =  {1, 2, 3020, 4, 22, 'alex', 3, 'rain', 'alex', 'python'}
print(len(set_f3))
# 9

# clear 清空
set_f4 = set_f3.clear()
print(set_f4)


'''
判断元素是否在集合中存在
语法格式如下：

x in set
'''
set_f5 = {1, 2, 3020, 4, 22, 'alex', 3, 'rain', 'alex', 'python'}

if ('alex' in set_f5):
    print('True')
else:
    print('false')
# True

if ('Youtube' in set_f5):
    print('True')
else:
    print('false')

# false


'''
add为集合添加元素
clear移除集合中的所有元素
copy拷贝一个集合
difference返回多个集合的差集
difference_update移除集合中的元素，该元素在指定的集合也存在。
discard删除集合中指定的元素
intersection返回集合的交集
intersection_update返回集合的交集。
isdisjoint判断两个集合是否包含相同的元素，如果没有返回True，否则返回False。
issubset判断指定集合是否为该方法参数集合的子集。
issuperset判断该方法的参数集合是否为指定集合的子集
pop随机移除元素
remove移除指定元素
symmetric_diference       返回两个集合中不重复的元素集合。
symmetric_difference_update 移除当前集合中在另外一个指定 集合相同的元素，并将另外-个指定集合中不同的元素插入到当前集合中。
union 返回两个集合的并集 
update 给集合添加元素
'''