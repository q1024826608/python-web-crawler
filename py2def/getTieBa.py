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
# 存到本地
class Savehtml2File:
    def __init__(self,htmlcontent,filename):
        self.content = htmlcontent
        self.filename = filename
    def save2local(self):
        output = open(self.filename,"w+")
        output.write(self.content)
        output.close()

count = 50

while count<1000:
    myhtml = GetHtml('http://tieba.baidu.com/f?kw=石家庄铁道大学&ie=utf-8&pn='+str(count))
    htmlcontent = myhtml.getHtmlContent()
    count = count + 50
    text = ''
    soup = BeautifulSoup(htmlcontent, "html.parser")
    # <a rel="noreferrer" href="/p/5475345316" title="回来溜达一圈" target="_blank" class="j_th_tit ">回来溜达一圈</a>
    for k in soup.find_all('a',class_="j_th_tit"):
        text = text + k['href'] + '\n'
    
    urls = text.split('\n')
    for url in urls:
        filename = url.replace('/','')
        urlbase = 'http://tieba.baidu.com'
        url = urlbase + url
        print url,'开始获取'
        htmlcontent = GetHtml(url).getHtmlContent()
        soup1 = BeautifulSoup(htmlcontent, "html.parser")
        [s.extract() for s in soup1('script')] # 删除页面script标签
        soup1.style.decompose()
        text = soup1.get_text().replace("\n"," ")    # 获取页面所有文本内容
        text = '\n'.join(filter(lambda x: x, text.split(' ')))
        Savehtml2File(text,'tiezi/'+filename+'.txt').save2local()
