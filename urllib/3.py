import urllib.request

url="http://www.jd.com/"
info=urllib.request.urlopen(url).info()
# print(dir(info))
print(info)
print(info.get_content_charset())