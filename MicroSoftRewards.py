import requests
import os
import lxml
import urllib.parse

from win32api import Sleep

if __name__=="__main__":

    url = "https://cn.bing.com/search?"
    mobileCookies = 't'
    with open("mobileCookies.txt",mode='r',encoding='utf-8') as fp:
        mobileCookies = fp.read().rstrip()
    print(mobileCookies)
    words = ''
    with open('SearchWords.txt', mode='r', encoding='utf-8') as fp1:
        words = fp1.readlines()

    n = len(words)
    for i in range(n):
        words[i] = words[i].rstrip()
    print(words)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; 16s Pro) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
        'Cookie': mobileCookies,
    }
    searchData = 'listen1'
    paramData = {
        'q': searchData
    }
    # name = '墨'
    # location = '南岗区，黑龙江省'
    # name1 = urllib.parse.quote(name)
    # location1 = urllib.parse.quote(location)
    # print(name1)
    # print(location1)
    for i in range(n):
        paramData['q'] = words[i]
        print(words[i])
        text = requests.get(url=url, headers=headers, params=paramData).text
        Sleep(10)
    # 加砖我修改了我在秀嘎f
    # print(text)

