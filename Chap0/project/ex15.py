# -*- coding:utf-8 -*-
from sys import argv
script, filename = argv

# 打开.txt格式文件
txt = open(filename)

# 提示加读取文件内容
print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")

file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())