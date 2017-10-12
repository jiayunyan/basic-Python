import urllib.request
url="http://blog.csdn.net/drdairen/article/details/51149498/"
# html=urllib.request.urlopen(url)
# print(html.read())
# print(html.getcode())
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
req.add_header("GET","http://blog.csdn.net/drdairen/article/details/51149498/")
req.add_header("HOST","blog.csdn.net")
req.add_header("Referer","http://blog.csdn.net/")
html=urllib.request.urlopen(req)
print(html.read().decode())