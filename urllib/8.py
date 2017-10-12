import urllib.request
from bs4 import BeautifulSoup

def get_content(url):
    html=urllib.request.urlopen(url)
    content=html.read().decode()
    html.close()
    return content

def get_images(info):
    soup=BeautifulSoup(info, "html.parser")
    all_img=soup.find_all('img',class_="BDE_Image")
    # return [img['src'] for img in all_img]
    i=1
    for img in all_img:
        print(img['src'])
        urllib.request.urlretrieve(img['src'], 'F:\\%s.jpg' % i)
        i+=1



info=get_content("http://tieba.baidu.com/p/5096144918?red_tag=j0230121706")
print (get_images(info))