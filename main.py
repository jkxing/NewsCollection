import requests
import re
from pyquery import PyQuery as pq
import time
from urllib import request,parse,error
from urllib.parse import urlparse
homeUrl = "http://www.xinhuanet.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'www.xinhuanet.com'
}


def get_detail(url,name):

    res = requests.get(url, headers = headers)
    html = res.content.decode('utf8')
    doc = pq(html)
    detail = doc('#p-detail')
    if detail.size() == 0 :
        print("no p-datail")
    else:
        print(doc('title').text(),url)
        with open(name,"w",encoding='utf-8') as f:
            f.write(detail.text())
    return

def getPageUrls(url):
    urllist = []
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf8')
    doc = pq(html)
    doc = doc('a')
    for item in doc.items():
        if item.attr('href')!=None:
            urllist.append(item.attr('href'))
    #print(urllist)
    return urllist

def filt(url):
    #print(url)
    #result = urlparse(url)
    #netloc = result.netloc
    urlPattern = re.compile("http://www\.xinhuanet\.com",re.S)
    if re.match(urlPattern,url):
        return 0;
    return 1;


dic = dict()
urllist = []
urllist.append(homeUrl)
detailNum=0
# get_detail(url,'1.html')
while len(urllist) > 0:
    url = urllist.pop(0)
    if url in dic:
        continue
    dic[url]=1
    urltype = filt(url)
    if urltype == 0:
        detailNum = detailNum + 1
        get_detail(url , str(detailNum)+".html")
        urllist.extend(getPageUrls(url))
    time.sleep(0.001)


# textPattern = re.compile("<p>(.*?)</p>",re.S)
# textList = re.findall(textPattern,detail.text())
# for item in textList:
#    print(type(item))


