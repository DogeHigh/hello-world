#亚马逊 https://www.amazon.cn/gp/product/B01M8L5Z3Y
import requests
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
kv={'user-agent':'Mozilla/5.0'}
try:
    r=requests.get(url,headers=kv)#修改request头部信息
    r.raise_for_status()#在返回不是200时产生异常
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败amazon")
