# 字符串基本概念
'''
如下定义的变量a，存储的是数字类型的值

    a = 100
如下定义的变量b，存储的是字符串类型的值

    b = "hello itcast.cn"
    或者
    b = 'hello itcast.cn'
小总结：

双引号或者单引号中的数据，就是字符串
'''

# 字符串输入输出 
# 与普通的输入输出基本相同
#demo1 输出

name = 'xiaoming'
position = '讲师'
address = '北京市'

print('--------------------------------------------------')
print("姓名：%s"%name)
print("职位：%s"%position)
print("公司地址：%s"%address)
print('--------------------------------------------------')

#demo2 输入

userName = input('请输入用户名:')
print("用户名为：%s"%userName)

password = input('请输入密码:')
print("密码为：%s"%password)


# 字符串下标切片

# 下标
'''
字符串中"下标"的使用

列表与元组支持下标索引好理解，字符串实际上就是字符的数组，所以也支持下标索引。

相当于C语言中的字符数组 数组是从下标0开始的

int array[]="helloVscode"

array[0]='h'
array[1]='e'
array[2]='l'
array[3]='l'
array[4]='o'
'''

Str = 'helloVscode'
print(Str[0])
print(Str[10])
# 格式化输出
print("Str[1]=%s"%Str[1])
print("Str[5]=%s"%Str[5])
print("Str[9]=%s"%Str[9])
'''
结果 
h
e
Str[1]=e
Str[5]=V
Str[9]=d
'''

'''
切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。

切片的语法：[起始:结束:步长]
注意：选取的区间属于左闭右开型，即从"起始"位开始，到"结束"位的前一位结束（不包含结束位本身)
'''

# demo
# 切片的语法：[起始:结束:步长]
# str = [N0:Nn:Step] 前闭后开

String = 'Vscode_Python'  
# 从左往右  0--》》
# 从右往左  《《--1
# 步长 Step 默认为1(可以省略不写) 
# [::1] 默认 从0到最后一个
# 步长 Step>0 顺序方向 Step<0 逆序方向
print(String[0:6:1]) 

print(String[7:13:1]) 

print(String[::-1])
print(String[1:-1])
# a[5:1:-2]
print(String[5:0:-2])


'''
结果
Vscode
Python
nohtyP_edocsV
scode_Pytho
eos
'''



# 给定一个字符串aStr, 请反转字符串

str1="aStr"
reverse = str1[::-1]  
print(reverse)
