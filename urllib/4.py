import urllib.request
import chardet
# url="http://www.iplaypython.com/"
# comment=urllib.request.urlopen(url).read()
# print(chardet.detect(comment))
def automatic_detect(url):
    comment = urllib.request.urlopen(url).read()
    result=chardet.detect(comment)
    encoding=result['encoding']    #取字典里的值
    return encoding

urls=["http://www.iplaypython.com/","http://www.163.com/","http://www.jd.com/"]
for url in urls:
    print(url,automatic_detect(url))