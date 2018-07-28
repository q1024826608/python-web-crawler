# -*- coding=utf-8 -*-
# -*- coding=utf-8 -*-
# author vvyun

'''
python 获取一些漂亮的图片
'''

import urllib.request
import re
import json

def getcontent(url):
    '''获取链接html内容'''
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode('utf-8')
    return data

def savestr2file(filename, content):
    '''存储字符串到文件'''
    output = open(filename, "w+", encoding='utf8')
    output.write(content)
    output.close()

def getcateloagarray(content):
    '''获取4chan - catalog数据   ---var catalog = {......};var style_group---'''
    pattern = r"var\scatalog\s=(.*).var\sstyle_group"
    res = re.search(pattern, content, re.M | re.S)
    return res.group(1)

def getimageurls(content):
    '''获取网页中的图片链接 <a href="//is2.4chan.org/a/1532677483030.jpg" '''
    pattern = r'<a\shref=\"..is2.4chan.org/a/(.*?\.[j|p|g][p|n|i][g|f])\".*?>'
    res = re.findall(pattern, content)
    return res

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
#  检验url是否可以正常访问
def getHttpStatusCode(tempUrl):
    '''检验url是否可以正常访问'''
    try :
        opener.open(tempUrl)
        # print(tempUrl+'没问题')
        return 0
    except urllib.error.HTTPError:
        print(tempUrl+'=访问页面出错')
        return 1
    except urllib.error.URLError:
        print(tempUrl+'=访问页面出错')
        return 2

mokuaibase = ['a','e','ck']
basec = "a"

urlindexbase = "https://boards.4chan.org/"+basec+"/catalog"
urlthreadbase = "https://boards.4chan.org/"+basec+"/thread/"
urlimgbase = "https://i.4cdn.org/"+basec+"/"
urlimgbase_a = "https://is2.4chan.org/a/"

print("indexpage:"+urlindexbase)
content = getcontent(urlindexbase)
filename = "image/content.html"
savestr2file(filename, content)

cateloageindex = getcateloagarray(content)
filenameimg = "image/cateloageindex.json"
savestr2file(filenameimg, cateloageindex)

cateloageindex = json.loads(cateloageindex)["threads"]
for threadnum in cateloageindex:
    print(urlthreadbase+threadnum)
    # if getHttpStatusCode(urlthreadbase+threadnum)>0:
    #     continue
    content = getcontent(urlthreadbase+threadnum)
    filename = "image/html/"+threadnum+".html"
    savestr2file(filename, content)
    imagedata = getimageurls(content)
    for iu in imagedata:
        # print(iu+"/n")
        imd = urlimgbase_a + iu
        print(imd)
        try:
            if getHttpStatusCode(imd)<1:
                urllib.request.urlretrieve(imd, "image/data/" + iu)
        except Exception as e:
            raise e
    # imagedata = getcateloagarray(content)
    # imagedata = json.loads(imagedata)["threads"]
    # for iurl in imagedata:
    #     # print(iurl)
    #     icontent = imagedata[iurl]
    #     imd = urlimgbase + icontent["imgurl"] + ".jpg"
    #     print(imd)
    #     try:
    #         if getHttpStatusCode(imd)<1:
    #             urllib.request.urlretrieve(imd, "image/data/" + icontent["imgurl"]+'.jpg')
    #     except Exception as e:
    #         raise e