# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C(^C).")
print ("If you do want that, hit RETURN.")

input("?")

# 打开文件，格式为写入 write
print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
# 对 target 执行截断
target.truncate()

print ("Now I'm going to ask ypou for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

input("?")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()