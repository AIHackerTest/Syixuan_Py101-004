# -*- coding: utf-8 -*-
 
import random
secret = random.randint(1,20)
guess = 0
tries = 0
print("猜一个数字，在 1 到 20 内，你有 10 机会！开始吧，少年！")

while guess != secret and tries < 10:
	guess = int(input("> "))
	if not guess : break
	if guess < secret:
		print("你猜小了")
	elif guess > secret:
		print("你猜大了")
	tries = tries + 1
if guess == secret:
	print("你猜对了！")
else:
	print("没机会了！")

#规则
# 程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
# 程序根据用户输入，给予一定提示（大了、小了、正确）
# 猜对或用完 10 次机会，游戏结束