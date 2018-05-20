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

myhtml = GetHtml('http://tieba.baidu.com/p/5473636248')
htmlcontent = myhtml.getHtmlContent()
# print htmlcontent
soup = BeautifulSoup(htmlcontent, "html.parser")
[s.extract() for s in soup('script')] # 删除页面script标签
soup.style.decompose()
text = soup.get_text().replace("\n"," ")    # 获取页面所有文本内容
text = '\n'.join(filter(lambda x: x, text.split(' ')))
Savehtml2File(text,'10001').save2local()



