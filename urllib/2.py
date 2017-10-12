# -*-coding: utf-8-*-
import urllib.request
def callback(a,b,c):
    process=100.0*a*b/c
    if process>100:
        process=100
    print("%.2f%%"%process,end=' ')
def callback1(*a):
    print(a)
url="http://www.iplaypython.com/"
url2="http://www.python.org/"
html=urllib.request.urlopen(url)
local='F:\\ipython.html'
urllib.request.urlretrieve(url2,local,callback1)