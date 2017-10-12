import re
import urllib.request
def get_content(url):
    html=urllib.request.urlopen(url)
    content=html.read().decode()
    html.close()
    return content

def get_images(info):
    regex= 'img class="BDE_Image" pic_type="0" width=".+?" height=".+?" src="(.+?\.jpg)"'
    pat=re.compile(regex)
    images_code=re.findall(pat,info)
    # return images_code
    i=0
    for images_url in images_code:
        print(images_url)
        urllib.request.urlretrieve(images_url,'F:\\%s.jpg'%i)
        i+=1

info=get_content("http://tieba.baidu.com/p/5096144918?red_tag=j0230121706")
get_images(info)
