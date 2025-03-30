# name='KI'
# age=20
# sex='man'
# print('我叫{},今年{}岁,性别是：{}'.format(name,age,sex))
from multiprocessing.util import MAXFD

# F=int(input("please input the temputre:"))
# C=int((F-32)*5/9)
# print("the temputre is:",C)

# Gread=input('please input your gread:')
# P,M,X,E =map(float,Gread.split( ))
# SUM=P+M+X+E
# AVG=(P+M+X+E)/4
# print("总和为：",SUM,
#       "平均值：",AVG,
#       '最大值{}，最小值{}'.format(max(P,E,M,X),min(P,E,M,X)))

'''
取个位-----除以10的模  a%10
取十位-----(a//10)%10
取百位-----a//100
'''
# a=int(input("请输入四位数a的值："))
# b=a//1000
# x=(a//100)%10
# y=(a//10)%10
# z=a%10
#
# print("a的个位为：{}".format(z))
# print("a的十位为：{}".format(y))
# print("a的百位为：{}".format(x))
# print("a的千位为：{}".format(b))

x="Learning Python makes happy"
print("出现次数：x.count('e')=",x.count('e'))
print("",x.isspace())
print("",x.isupper())
print("",x.isalnum())
print("填充a值:x.rjust(15,'+')=",x.rjust(45,'+'))