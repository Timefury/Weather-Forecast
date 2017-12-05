# -*- coding: utf-8 -*-
# windows 下如果出现编码问题，将 utf-8 改为 gbk


import urllib
import gzip
import json
# from StringIO import StringIO

while True:
    # 获取网页返回
    city = input('请输入要查询的城市（直接回车退出）：\n')
    if not city:
        break
    # city = city.decode('gbk').encode('utf-8')  # windows 控制台下输入需转换编码

    url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % city

    # 因网页内容做了 gzip 压缩，所以要对其解压， 发现没有做gizp压缩，省去这一步。
    '''
    try:
        buf = StringIO(resp)
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
    except:
        data = resp
    # print data
    '''

    import requests

    resp = requests.get(url)
    result = resp.json()
    result_data = result.get('data')
    # print result_data

    if result_data:
        print('当前温度：', result_data.get('wendu'), '℃')
        print('空气质量：', result_data.get('aqi'))
        print(result_data.get('ganmao'))
        # print result_data.get('ganmao').decode('utf-8').encode('gbk')  # windows 编码参考

        print('5日天气预报：')
        forecast = result_data.get('forecast')
        for fc in forecast:
            print(fc.get('date'), '：', fc.get('type'), '，', fc.get('low'), '，', fc.get('high'))
    else:
        print('未能获取此城市的天气情况。')
    print