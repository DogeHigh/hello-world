import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()
        return ""

def getStockList(lst,stockURL):
    html=getHTMLText(stockURL)
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    count=0
    for i in a:
        count=count+1
        print("爬取股票1-%s"%count)
        try:
            href=i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    count=0
    for stock in lst:
        url = stockURL + stock +".html"
        count=count+1
        print("爬取股票2-%s"%count)
        print(url)
        html =getHTMLText(url)
        try:
            if html =="":
                print("空的？")
                continue
            infoDict={}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})
            name=stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
           
            for i in range(len(keyList)):
                
                key=keyList[i].text
                val=valueList[i].text
                infoDict[key]=val
                #print("%s,%s"%key%val)
                print(key+","+val)
                
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
        except:
            traceback.print_exc()
            continue
    return ""

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://BaiduStockInfo.txt'
    slist = []
    with open(output_file,'a',encoding='utf-8') as f:
                f.write("股票数据爬取\n")
    print("爬取股票1")
    getStockList(slist,stock_list_url)
    print("爬取股票2")
    getStockInfo(slist,stock_info_url,output_file)
    print("爬取股票3")

main()
