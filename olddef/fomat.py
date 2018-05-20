# -*- coding=utf-8 -*-
# @author NuageVoler
# @update 18-4-7
import urllib2
import urllib
import re
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

# 获取内容
class GetHtml:
    def __init__(self, htmlurl):
        self.htmlurl = htmlurl
    def getHtmlContent(self):
        url = self.htmlurl
        try:
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            content=response.read().decode("utf-8")
            # print content  #测试输出
            return content
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print e.reason


class Savehtml2File:
    def __init__(self,htmlcontent,filename):
        self.content = htmlcontent
        self.filename = filename
    def save2local(self):
        output = open(self.filename,"w+")
        output.write(self.content)
        output.close()

myhtml = GetHtml('http://tieba.baidu.com/f?kw=石家庄铁道大学&ie=utf-8&pn=0')
htmlcontent = myhtml.getHtmlContent()
text = ''
# print htmlcontent
soup = BeautifulSoup(htmlcontent, "html.parser")
# [s.extract() for s in soup('script')] # 删除页面script标签
# [s.extract() for s in soup('link')]
# [s.extract() for s in soup('meta')]
# [s.extract() for s in soup('a')]
# [s.extract() for s in soup('table')]
# soup.style.decompose()
# text = soup.prettify()
# text = soup.get_text().replace("\n"," ")    # 获取页面所有文本内容
# text = '\n'.join(filter(lambda x: x, text.split(' ')))

for k in soup.find_all('div',class_="threadlist_lz clearfix"):
    # print(k)#查a标签的string
    # text = text  + k.get_text() + '\n'
    for child in k.find_all('a',class_="j_th_tit"):
        text = text + child['href'] + '\n'
    for child in k.find_all('span',class_="pull-right is_show_create_time"):
        text = text + child.get_text() + '\n'
       
Savehtml2File(text,'res').save2local()