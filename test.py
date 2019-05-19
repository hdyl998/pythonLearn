# coding=UTF-8（等号换为”:“也可以）
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

def content(html):
    str = '<article class="article-content">'
    content = html.partition(str)[2]
    str1 = '<div class="article-social">'
    content = content.partition(str1)[0]
    return content

# text=raw_input("按下 enter 键退出，其他任意键显示...\n")

# 空字符串，都是假的
text=""
text=0

print text
if text:
    print "True"
else:
    print "False"

item_one = '1'
item_two = '2'
item_three = '3'
total = item_one + \
        item_two + \
        item_three
print total
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

print days
print paragraph

print content('<article class="article-content">ffaaff<div class="article-social">')


if False:
    print "True"
elif True:
    print "ttt"
else:
    print "False"

# if True:
#     print "Answer"
#     print "True"
# else:
#     print "Answer"
#     # 没有严格缩进，在执行时会报错
#     print "False"


aaa = '''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

ccc = """
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
print aaa;
print ccc;



x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y
print x,

# //同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')