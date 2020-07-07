# 字符串常见操作

# 字符串 方法
'''
capitalize()	把首字符转换为大写。
casefold()	把字符串转换为小写。
center()	返回居中的字符串。
count()	返回指定值在字符串中出现的次数。
encode()	返回字符串的编码版本。
endswith()	如果字符串以指定值结尾，则返回 true。
expandtabs()	设置字符串的 tab 尺寸。
find()	在字符串中搜索指定的值并返回它被找到的位置。
format()	格式化字符串中的指定值。
format_map()	格式化字符串中的指定值。
index()	在字符串中搜索指定的值并返回它被找到的位置。
isalnum()	如果字符串中的所有字符都是字母数字，则返回 True。
isalpha()	如果字符串中的所有字符都在字母表中，则返回 True。
isdecimal()	如果字符串中的所有字符都是小数，则返回 True。
isdigit()	如果字符串中的所有字符都是数字，则返回 True。
isidentifier()	如果字符串是标识符，则返回 True。
islower()	如果字符串中的所有字符都是小写，则返回 True。
isnumeric()	如果字符串中的所有字符都是数，则返回 True。
isprintable()	如果字符串中的所有字符都是可打印的，则返回 True。
isspace()	如果字符串中的所有字符都是空白字符，则返回 True。
istitle()	如果字符串遵循标题规则，则返回 True。
isupper()	如果字符串中的所有字符都是大写，则返回 True。
join()	把可迭代对象的元素连接到字符串的末尾。
ljust()	返回字符串的左对齐版本。
lower()	把字符串转换为小写。
lstrip()	返回字符串的左修剪版本。
maketrans()	返回在转换中使用的转换表。
partition()	返回元组，其中的字符串被分为三部分。
replace()	返回字符串，其中指定的值被替换为指定的值。
rfind()	在字符串中搜索指定的值，并返回它被找到的最后位置。
rindex()	在字符串中搜索指定的值，并返回它被找到的最后位置。
rjust()	返回字符串的右对齐版本。
rpartition()	返回元组，其中字符串分为三部分。
rsplit()	在指定的分隔符处拆分字符串，并返回列表。
rstrip()	返回字符串的右边修剪版本。
split()	在指定的分隔符处拆分字符串，并返回列表。
splitlines()	在换行符处拆分字符串并返回列表。
startswith()	如果以指定值开头的字符串，则返回 true。
strip()	返回字符串的剪裁版本。
swapcase()	切换大小写，小写成为大写，反之亦然。
title()	把每个单词的首字符转换为大写。
translate()	返回被转换的字符串。
upper()	把字符串转换为大写。
zfill()	在字符串的开头填充指定数量的 0 值。
'''

# find 判断某个字符串是否在其他字符串里面出现
MyStr = 'HelloPython VscodePython Python Anconda Pythondeeplearning AI OpenCV PythonCSS'
mystr = MyStr.find("Vscode")
mystr2 = MyStr.find("Python")
print(mystr)
print(mystr2)
'''
MyStr.find()

find(sub, start=0, end=-1)

str.find(str, beg=0, end=len(string))

str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。

如果包含子字符串返回开始的索引值，否则返回-1。

'''

# index
# 与 find()方法一样，只不过如果str不在 mystr中会报一个异常
mystr = MyStr.index("Vscode")
print(mystr)

'''
index()方法语法：

index(sub, start=0, end=-1)
S.index(sub[, start[, end]]) -> int

str.index(str, beg=0, end=len(string))
参数
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。

返回值
如果包含子字符串返回开始的索引值，否则抛出异常.

'''

'''
结果：
Traceback (most recent call last):
  File "e:/Desktop/Code/python/Basic/str2.py", line 26, in <module>
    mystr = MyStr.index("Vscde")
ValueError: substring not found
'''


'''
count
返回 str在start和end之间 在 mystr里面出现的次数

ount()方法语法：

str.count(sub, start= 0,end=len(string))

参数
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

返回值
该方法返回子字符串在字符串中出现的次数。

'''
mycount = MyStr.count(' ') # 空格出现次数
print(mycount) 

'''
replace()方法语法：

str.replace(old, new[, max])
参数
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
返回值
返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
'''
mystr3  = 'HelloPython VscodePython Python Anconda Pythondeeplearning AI OpenCV PythonDjanjo Pythonrqequest'
print(MyStr)
print(mystr3)

myreplace = MyStr.replace('Python','pythontest',)
print(myreplace)
myreplace1 = mystr3.replace('Python','LearningPython',3) 

# old 要被替代的字符串
# new 新的字符串，你现在需要的字符串
# max: Maximum times 替换的最大次数不超过 Max
print(myreplace1)

'''
结果
Hellopythontest Vscodepythontest pythontest Anconda pythontestdeeplearning AI OpenCV pythontestCSS
HelloLearningPython VscodeLearningPython LearningPython Anconda Pythondeeplearning AI OpenCV PythonDjanjo Pythonrqequest
'''


'''
split
以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串

语法
split() 方法语法：

str.split(str="", num=string.count(str)).

参数

str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。

返回值
返回分割后的字符串列表

'''
mystr4  = 'HelloPython VscodePython Python Anconda deeplearningAI OpenCV PythonDjanjoPythonrqequest'
mysplit = mystr4.split(' ') #  默认为 -1, 即分隔所有。
mysplit2 =mystr4.split(' ',3) # 拆分的个数
print(mysplit)
print(mysplit2)

'''
结果
['HelloPython', 'VscodePython', 'Python', 'Anconda', 'deeplearningAI', 'OpenCV', 'PythonDjanjoPythonrqequest']
['HelloPython', 'VscodePython', 'Python', 'Anconda deeplearningAI OpenCV PythonDjanjoPythonrqequest']

'''


 
# 第二个参数为 1，返回两个参数列表
# 以下实例以 # 号为分隔符，指定第二个参数为 1，返回两个参数列表
txt = "Google#Runoob#Taobao#Facebook"
x = txt.split("#", 1)
y = txt.split('#',)

print(x)
print(y)

'''
结果：
['Google', 'Runoob#Taobao#Facebook']
['Google', 'Runoob', 'Taobao', 'Facebook']
'''

'''
capitalize
把字符串的第一个字符大写

Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。

语法
capitalize()方法语法：

str.capitalize()

返回值
该方法返回一个首字母大写的字符串。
'''

mystr5 = 'learnPython'
mycapitalize = mystr5.capitalize()
print(mycapitalize)

'''
title
把字符串的每个单词首字母大写
'''
# demo 

mystr6 = 'helloPython vscodePython python anconda deeplearningAI openCV pythonDjango pythonrqequest'
mytitle = mystr6.title()
print(mystr6)
print(mytitle)

'''
结果：
helloPython vscodePython python anconda deeplearningAI openCV pythonDjango pythonrqequest
Hellopython Vscodepython Python Anconda Deeplearningai Opencv Pythondjango Pythonrqequest
'''

'''
定义和用法
如果字符串以指定的值开头，则 startswith() 方法返回 True，否则返回 False。

语法
string.startswith(value, start, end)

参数
value	必需。检查字符串是否以其开头的值。
start	可选。整数，规定从哪个位置开始搜索。
end	可选。整数，规定结束搜索的位置。

'''

txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)
y = txt.startswith("ssr")
print(x)
print(y)
'''
结果:
True
False
'''

'''
endswith
如果字符串以指定值结尾，则 endswith() 方法返回 True，否则返回 False。

语法
string.endswith(value, start, end)

参数	
value	必需。检查字符串是否以之结尾的值。
start	可选。整数。规定从哪个位置开始检索。
end	可选。整数。规定从哪个位置结束检索
'''

txt = "Hello, welcome to my world."
txt1 = '2020-07-07 Learnpython'

x = txt.endswith("my world.", 5, 11)
y =txt1.endswith('python')
print(x) # False 
print(y) # True


'''
Python lower() 方法转换字符串中所有大写字符为小写

str.lower()

返回值

返回将字符串中所有大写字符转换为小写后生成的字符串
'''

str7 = "THIS IS STRING EXAMPLE....WOW!!!";

print(str7.lower())

'''
结果：
this is string example....wow!!!
'''

'''
Python upper() 方法将字符串中的小写字母转为大写字母。

返回值
返回小写字母转为大写字母的字符串。
'''

str8 = "this is string example....wow!!!"

print(str8.upper())

'''
结果：
THIS IS STRING EXAMPLE....WOW!!!
'''

'''
Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。

str.ljust(width[, fillchar])
str.rjust(width[, fillchar])

参数
width -- 指定字符串长度。
fillchar -- 填充字符，默认为空格。

返回值
ljust: 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
rjust: 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
'''

str9 = "this is string example....wow!!!"

print(str9.ljust(50,'0'))
print(str9.rjust(50,'0'))

print(str9.ljust(50))
print(str9.rjust(50))

# l 左
# r 右
'''
结果：
this is string example....wow!!!000000000000000000
000000000000000000this is string example....wow!!!

this is string example....wow!!!
                  this is string example....wow!!!
'''

'''
lstrip
删除 mystr 左边的空白字符
Python lstrip() 方法用于截掉字符串左边的空格或指定字符。

str.lstrip([chars])

chars --指定截取的字符。

返回值
返回截掉字符串左边的空格或指定字符后生成的新字符串。

'''
str10 = "     this is string example....wow!!!     "
print(str10)
print(str10.lstrip())
str11 = "88888888this is string example....wow!!!8888888"
print(str11)
print(str11.lstrip('8'))

'''
     this is string example....wow!!!
this is string example....wow!!!

88888888this is string example....wow!!!8888888
this is string example....wow!!!8888888
'''

'''
Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）

str.rstrip([chars])

chars -- 指定删除的字符（默认为空格）

返回删除 string 字符串末尾的指定字符后生成的新字符串。

'''

str12 = "     this is string example....wow!!!     "
print(str12)
print(str12.rstrip()) 
str13 = "88888888this is string example....wow!!!8888888"
print(str13)
print(str13.rstrip('8'))

'''
结果：
     this is string example....wow!!!
     this is string example....wow!!!

88888888this is string example....wow!!!8888888
88888888this is string example....wow!!!
'''









