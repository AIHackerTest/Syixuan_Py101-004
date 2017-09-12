# -*- coding:utf-8 -*-

# 类似于 argv
def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
   
# this just takes one arguments
def print_one(arg1):
    print ("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
    print ("I got nothing.")

print_two("Sun","yixuan")
print_two_again("Sun","yixuan")
print_one("First!")
print_none()