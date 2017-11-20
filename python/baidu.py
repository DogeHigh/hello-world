#百度、360 搜索关键词提交
#http://www.baidu.com/s?wd=keyword
#http://www.so.com/s?q=keyword
import requests
kv={'wd':'Python'}
url="http://www.baidu.com/s"
try:
    r=requests.get(url,params=kv)
    r.raise_for_status()#在返回不是200时产生异常
    r.encoding=r.apparent_encoding
    print(r.request.url)
    print(len(r.text))
except:
    print("爬取失败")
