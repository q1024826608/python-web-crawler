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

myhtml = GetHtml('http://tieba.baidu.com/p/5088197799')
htmlcontent = myhtml.getHtmlContent()
text = ''
# print htmlcontent
soup = BeautifulSoup(htmlcontent, "html.parser")

for k in soup.find_all('div',class_="d_post_content j_d_post_content clearfix"):
    text = text  + k.get_text() + '\n'
      
Savehtml2File(text,'txt').save2local()