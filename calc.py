#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c = a * b
print "3 - c 的值为：", c

c = a / b
print "4 - c 的值为：", c

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print "6 - c 的值为：", c

#//取整除赋值运算符

print "7 - c 的值为：", 9.0 // 2  # 取整除 - 返回商的整数部分（向下取整）
print "7 - c 的值为：", -9.0 // 2  # 取整除 - 返回商的整数部分（向下取整）



print 4<>5   #这个运算符类似 !=

a=10
a**=2
print a
a//=3
print a


a = 0b00111100

b = 0b00001101


print a
print b

print bin(a)
print bin(b)

print bin(a&b)
print bin(a|b)

print bin(a^b)

print "------------"
print bin(0b1)
print bin(~0b1)
