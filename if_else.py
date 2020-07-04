# 判断语句和循环语句

'''
判断语句
1. if-else的使用格式

    if 条件:
        满足条件时要做的事情1
        满足条件时要做的事情2
        满足条件时要做的事情3
        ...(省略)...
    else:
        不满足条件时要做的事情1
        不满足条件时要做的事情2
        不满足条件时要做的事情3
        ...(省略)...

'''
# 案例

chePiao = 1
# 用1代表有车票，0代表没有车票
if chePiao == 1:
    print("有车票，可以上火车")
    print("终于可以见到Ta了，美滋滋~~~")
else:
    print("没有车票，不能上车")
    print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")



'''
从键盘输入刀子的长度，如果刀子长度没有超过10cm，则允许上火车，否则不允许上火车
'''

length = int(input('请刀子输入长度:')) # 字符转成整形数字
if (length > 10):
    print('不允许上火车')

else:
    print('允许上火车')


'''
if--elif-else 的语法格式

elif的功能

elif的使用格式如下:


    if  xxx1:
        事情1
    elif xxx2:
        事情2
    elif xxx3:
        事情3

说明:

    当xxx1满足时，执行事情1，然后整个if结束
    当xxx1不满足时，那么判断xxx2，如果xxx2满足，则执行事情2，然后整个if结束
    当xxx1不满足时，xxx2也不满足，如果xxx3满足，则执行事情3，然后整个if结束

'''

# 案例

score = int(input('请输入成绩:'))  # 字符转成整形数字

if score>=90 and score<=100:
    print('本次考试，等级为A')
elif score>=80 and score<90:
    print('本次考试，等级为B')
elif score>=70 and score<80:
    print('本次考试，等级为C')
elif score>=60 and score<70:
    print('本次考试，等级为D')
elif score>=0 and score<60:
    print('本次考试，等级为E，下次努力')


'''
注意点:elif 可以和else一起使用

# 注意点
       if 性别为男性:
           输出男性的特征
           ...
       elif 性别为女性:
           输出女性的特征
           ...
       else:
           第三种性别的特征
           ...

    说明:
        当 “性别为男性” 满足时，执行 “输出男性的特征”的相关代码
        当 “性别为男性” 不满足时，如果 “性别为女性”满足，则执行 “输出女性的特征”的相关代码
        当 “性别为男性” 不满足，“性别为女性”也不满足，那么久默认执行else后面的代码，即 “第三种性别的特征”相关代码

    elif必须和if一起使用，否则出错

'''

# if嵌套
'''
if嵌套的格式

    if 条件1:

        满足条件1 做的事情1
        满足条件1 做的事情2
        ...(省略)...

        if 条件2:
            满足条件2 做的事情1
            满足条件2 做的事情2
            ...(省略)...

    说明
        外层的if判断，也可以是if-else
        内层的if判断，也可以是if-else
        根据实际开发的情况，进行选择

'''

# demo

chePiao = 1     # 用1代表有车票，0代表没有车票
daoLenght = int(input('输入刀子的长度:'))     # 刀子的长度，单位为cm

if chePiao == 1:
    print("有车票，可以进站")
    if daoLenght < 10:
        print("通过安检")
        print("终于可以见到Ta了，美滋滋~~~")
    else:
        print("没有通过安检")
        print("刀子的长度超过规定，等待警察处理...")
else:
    print("没有车票，不能进站")
    print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")

# demo 
'''
输入公交卡当前的余额，只要超过2元，就可以上公交车；如果空座位的数量大于0，就可以坐下
'''

Balance = int(input('请输入余额:'))
seatsNumber = int(input('请空座位的数量:'))

if (Balance > 2 ):
    print('可以上公交车')
    if (seatsNumber > 0):
        print('有空座位，可以坐下')
    else:
        print('没有空座位')
else:
    print('余额不足，不可以上公交车')


# 猜拳游戏demo
import random

player = input('请输入：剪刀(0)  石头(1)  布(2):')

player = int(player)

computer = random.randint(0,2)

# 用来进行测试
#print('player=%d,computer=%d',(player,computer))

if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print('获胜，哈哈，你太厉害了')
elif player == computer:
    print('平局，要不再来一局')
else:
    print('输了，不要走，洗洗手接着来，决战到天亮')