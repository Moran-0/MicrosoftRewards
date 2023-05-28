import requests
import os
import lxml
import urllib.parse
if __name__=="__main__":

    url = "https://cn.bing.com/search?"
    mobileCookies = 't'
    with open("mobileCookies.txt",mode='r',encoding='utf-8') as fp:
        mobileCookies = fp.read().rstrip()
    print(mobileCookies)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; 16s Pro) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
        'Cookie':mobileCookies,
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
    text = requests.get(url=url, headers=headers, params=paramData).text
    print(text)

