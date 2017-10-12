# -*-coding: utf-8-*-
import urllib.request
# print(dir((urllib.request)))
# print(help(urllib.request.urlopen))
url="http://www.iplaypython.com/"
html=urllib.request.urlopen(url)
print (html.read())
print(html.info())
print(html.getcode())
print(html.geturl())
html2=urllib.request.urlopen(url).read().decode()
print(html2)
