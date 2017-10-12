import urllib.request
url="http://blog.csdn.net/drdairen/article/details/51149498/"
myheaders={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "GET":"http://blog.csdn.net/drdairen/article/details/51149498/",
    "HOST":"blog.csdn.net",
    "Referer":"http://blog.csdn.net/"
}
req=urllib.request.Request(url,headers=myheaders)
html=urllib.request.urlopen(req)
# print(html.read().decode())
print(req.headers.items())