import requests
import json

history_list = []

def fetch_weather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': 'z0i3iccaxcyyxpyn',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout = 20)
    
    return result

def show_weather(jd):
    temperature = jd['results'][0]['now']['temperature']
    text = jd['results'][0]['now']['text']
    code = jd['results'][0]['now']['code']
    weather = f'\n{order} 温度：{temperature}\n天气状况：{text}\n天气指数：{code}\n'
    
    return weather

def help():
    print(
        '''
        输入城市名，查询该城市的天气；
        输入 help，获取帮助文档；
        输入 history,获取查询历史；
        输入 quit，退出天气查询系统。
        '''
        )
        
while True:
    order = input('请输入你需要查询的城市名：')
    try:
        result = fetch_weather(order)
        jd = json.loads(result.text)
        weather = show_weather(jd)
        print(weather)
        history_list.append(weather)
        
    except KeyError:
        if order in ['h', 'help']:
            help()

        elif order in ['history']:
            for info in history_list:
                print(info)

        elif order in ['quit', 'q']:
            print("退出查询系统！")
            break
        
        else:
            print('没有该城市信息，请输入help获取帮助！')