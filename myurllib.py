from urllib import request,parse,error
from urllib.parse import urlparse

# print(response.read().decode('utf-8'))

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'learn.tsinghua.edu.cn'
}

dict = {
    'name': 'Germey'
}

url = 'http://www.baidu.com/index.html;user?id=5#comment'

data = bytes(parse.urlencode(dict), encoding='utf8')
try:
    #req = request.Request(url=url, data=data, headers=headers, method='POST')
    req = request.urlopen(url)
except error.URLError as e:
    print(e.reason)
    exit(0)

result = urlparse(url)
print(type(result),result)

exit(0)
response = request.urlopen(req)
print(response.read().decode('gb2312'))