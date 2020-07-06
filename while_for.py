'''
while循环的格式

    while 条件:
        条件满足时，做的事情1
        条件满足时，做的事情2
        条件满足时，做的事情3
        ...(省略)...

'''

# demo
i = 0
while i<5:
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i+=1

'''
while循环应用
1.计算1~100的累积和（包含1和100）
2.计算1~100之间偶数的累积和（包含1和100）
'''

# demo1 
num =1
sum = 0
while num<=100:
    num = num + 1
    sum = sum + num 
print(sum)

# demo2

fnum = 1
fsum = 0
while fnum <= 100:
    if (fnum%2 == 0):
        fsum = fsum + fnum
    fnum = fnum +1
        
print("1~100的累积和为:%d"%fsum)

# demo3
i = 1
sum = 0
while i<=100:
    if i%2 == 0:
        sum = sum + i
    i+=1
print("1~100的累积和为:%d"%sum)

'''
for 循环
格式:
for i in num:
    执行循环语句
'''

'''
for循环的格式

for 临时变量 in 列表或者字符串等:
  循环满足条件时执行的代码

'''

name = 'chengdu'
for x in name:
    print(x,end ='')




# break和continue
'''
break的作用：用来结束整个循环

'''

# for 循环中的break

# demo4

name = 'helloVscode'

for x in name:
    print('----')
    print(x)


#######################################
# demo5
print('##############################')
print('break')
name = 'helloVscode'

for x in name:
    print('----')
    if (x == 'V'):
        break
    print(x)

#####################################

# while 循环中的break

# demo6
i = 0

while i<10:
    i = i+1
    print('----')
    print(i)

i = 0
while i<10:
    i = i+1
    print('----')
    if(i>5):
        break
    print(i)

####################################
'''
continue的作用：用来结束本次循环，紧接着执行下一次的循环
'''
print('continue for')
# demo4
print('##############################')
name = 'helloVscode'

for x in name:
    print('----')
    print(x)


#######################################
# demo5
print('##############################')
print('break')
name = 'helloVscode'

for x in name:
    print('----')
    if (x == 'V'):
        continue
    print(x)

#####################################

# while 循环中的continue

# demo6
print('continue while')
i = 0

while i<10:
    i = i+1
    print('----')
    print(i)

i = 0
while i<10:
    i = i+1
    print('----')
    if(i==5):
        continue
    print(i)

####################################




'''
注意点
break/continue只能用在循环中，除此以外不能单独使用
break/continue在嵌套循环中，只对最近的一层循环起作用
'''


'''
while循环嵌套
 while 条件1:

        条件1满足时，做的事情1
        条件1满足时，做的事情2
        条件1满足时，做的事情3
        ...(省略)...

        while 条件2:
            条件2满足时，做的事情1
            条件2满足时，做的事情2
            条件2满足时，做的事情3
            ...(省略)...
'''

'''
demo
 1.打印图形
 2.九九乘法表(经典案例)
'''
# 1.打印图形
'''

*
* *
* * *
* * * *
* * * * *

'''
# row 行 col 列

row= 1
while row<=5:
    col = 1
    while col <= row:
        print('*',end='')
        col = col +1
    print('\n')
    row = row +1

# 九九乘法表(经典案例)
i = 1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=%-2d "%(j,i,i*j),end='')
        j+=1
    print('\n')
    i+=1

'''
print("\t",end='');

包含end=''作为print()BIF的一个参数，会使该函数关闭“在输出中自动包含换行”的默认行为。
其原理是：为end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。
这个只有Python3有用，Python2不支持

'''

'''
 import 与 from...import

在 python 用  import 或者  from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为：  import somemodule
从某个模块中导入某个函数,格式为：  from somemodule import somefunction
从某个模块中导入多个函数,格式为：  from somemodule import firstfunc, secondfunc,
thirdfunc
将某个模块中的全部函数导入，格式为：  from somemodule import
'''
