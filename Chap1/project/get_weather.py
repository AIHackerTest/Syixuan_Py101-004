# -*- coding: utf-8 -*-

weather = {}
history = {}

with open('C:\\Users\\LENOVO\\Py101-004\\Chap1\\resource\\weather_info.txt', 'r', encoding = 'UTF-8') as f:
    for line in f.readlines():
        key = line.split(',')[0]
        value = line.split(',')[1].rstrip('\n')
        weather[key] = value
        # print(weather)  测试 list 是否转成 dict
        # print('{}:{}'.format(key, value))

def get_help():
    print ('''
    输入城市名称，搜索城市天气
    输入‘help’或 ‘h’，获得更多帮助
    输入‘history’，获得先去查询记录
    输入‘exit’，退出程序
    ''')

def get_history():
    for key, value in history.items():
        print('{}:{}'.format(key, value))

def get_weather_info():
    try:
        print('{} 天气：{}'.format(city, weather[city]))
        history[city] = weather[city]
    except:
        print("抱歉，你输入的城市不存在！")
        get_help()

while True:
    city = input("请输入城市的名称: ")
    if city == "help" or city == 'h':
        get_help()
    elif city == 'history':
        get_history()
    elif city == 'exit':
        exit(0)
    else:
        get_weather_info()