# -*- coding=utf-8 -*-

import main.htmltool as html_tool
from bs4 import BeautifulSoup


# 获取帖子链接
def geturls(baseurl, count):
    htmlcontent = html_tool.getcontent(baseurl + str(count))
    if htmlcontent is None:
        print("获取页面pn=" + count + "异常 ! ")
        return "error"
    soup = BeautifulSoup(htmlcontent, "html.parser")
    text = ''
    for tiezi in soup.find_all('div', class_="threadlist_lz clearfix"):  # 获取所有帖子
        for child_link in tiezi.find_all('a', class_="j_th_tit"):  # 获取帖子链接
            text = text + child_link['href'] + '\t'
        for child_time in tiezi.find_all('span', class_="pull-right is_show_create_time"):  # 帖子创建时间
            text = text + child_time.get_text() + '\n'
    return text


# 获取帖子内容
def gettext(url):
    html_content = html_tool.getcontent(url)  # 获取网页内容
    if html_content is None:
        print("获取页面异常 ! ")
        return "error"
    soup = BeautifulSoup(html_content, "html.parser")
    text = ''
    for tiezi in soup.find_all('div', class_="d_post_content j_d_post_content clearfix"):
        text = text + tiezi.get_text() + '\n'
    return text


# 获取网页内容
def gethtml(url):
    htmlcontent = html_tool.getcontent(url)  # 获取网页内容
    if htmlcontent is None:
        print("获取页面异常 ! ")
        return "error"
    return htmlcontent

# baseurl = 'http://tieba.baidu.com/f?kw=%E7%9F%B3%E5%AE%B6%E5%BA%84%E9%93%81%E9%81%93%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
# print(geturls(baseurl,0))
