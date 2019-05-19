#!/usr/bin/python
# -*- coding: UTF-8 -*-
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter
print miles
print name


a = b = c = 1


a, b, c = 1, 2, "john"

print a,b,c


var1 = 1
var2 = 10
var,var_a,var_b=3,4,5

print var1,var2

del var
del var_a, var_b
# 删除引用后就不能使用了
# print var_a,var_b


# Python有五个标准的数据类型：
#
#     Numbers（数字）
#     String（字符串）
#     List（列表）
#     Tuple（元组）
#     Dictionary（字典）

# Python支持四种不同的数字类型：
#
#     int（有符号整型）
#     long（长整型[也可以代表八进制和十六进制]）
#     float（浮点型）
#     complex（复数）

print 0x69L;
print 70.2E-12
print 4.53e-7j

s = 'abcdef'
# [头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。

print s[1:5]  #0-6 bcde
print s[-5:-1] #-6~-1

str = 'Hello World!'


print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第六个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

letters=['c','h','i','n','a']
print letters[1:4:2]

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

# Python 元组
#
# 元组是另一个数据类型，类似于 List（列表）。
#
# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第四个（不包含）的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组



tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

# 列表是有序的对象集合，字典是无序的对象集合。
#
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值