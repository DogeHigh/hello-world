#京东 https://item.jd.com/2967929.html
import requests
url="https://item.jd.com/2967929.html"
try:
    r=requests.get(url)
    r.raise_for_status()#在返回不是200时产生异常
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败jd")
