import requests
import lxml

if __name__=="__main__":

    url = "https://www.bilibili.com/"
    text = requests.get(url=url,).text
    print(text)