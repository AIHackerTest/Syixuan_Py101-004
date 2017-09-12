import random

def Num():
    num = random.sample(range(0,10),4)
    while num[0] == 0:
        num = random.sample(range(0,10),4)
    return num

number = Num()
times = 9


while times >=0:
    guess = input("输入一个四位数字：")
    get_num = []
    for x in guess:
        get_num.append(int(x))
    
    times -= 1

    a = 0
    c = 0
    for x in range(4):
        if number[x] == get_num[x]:
            a += 1
    for y in get_num:
        if y in number:
            c += 1
    b = c - a
    print("%dA%dB" % (a,b))
    print("你还有 %d 次机会" % times)
    if a == 4:
        print("恭喜你答对了！")

    if times < 0:
        print("正确答案是 %r" % number)
