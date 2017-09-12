# 利用心知天气API，获取天气
import requests

def fetch_weather(location):# 用requests库，与API交互并获取信息
    result = requests.get('https://api.seniverse.com/v3/weather/daily.json', params={
            'key': 'z0i3iccaxcyyxpyn',
            'location': location,
            'language': 'zh-Hans',
            'unit': ''
        }, timeout=30)
    result = result.json()
    daily = result['results'][0]['daily'][1]
    date = daily['date']
    text_day = daily['text_day']
    text_night = daily['text_night']
    high = daily['high']
    low = daily['low']
    wind_direction = daily['wind_direction']
    wind_scale = daily['wind_scale']
    weather_str = f'{date}：{location}白天{text_day}，夜晚{text_night}。
    最高气温{high}度，最低气温{low}度。{wind_direction}风{wind_scale}级。'
    return weather_str