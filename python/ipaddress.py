#IP归属地查询
#http://www.ip138.com/ips138.asp?action=2&ip=
import requests
url="http://www.ip138.com/ips138.asp?action=2&ip="
#kv={'ip':'ipaddress'}
ip="'200.204.80.112'"
try:
    r=requests.get(url+ip)
    print(r.staus_code)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
