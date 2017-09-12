# -*- coding:utf-8 -*-

from sys import argv

script, input_file = argv

# 读取文件并打印
def print_all(f):
    print (f.read())

# 执行 seek() 操作,转到第一个byte 位置
def rewind(f):
    f.seek(0)

# 打印一行
def print_a_line(line_count, f):
    print (line_count, f.readline())

# 将导入的文件值赋给 current_file
current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

# 调用 rewind() 函数，转到第一个 byte
rewind(current_file)

print ("Let's print three lines:")

# 调用 print_a_line() 函数
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)