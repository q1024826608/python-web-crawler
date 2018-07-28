# -*- coding=utf-8 -*-

import main.savefile as save_file
import main.bs4tool as bs4tool

baseurl = 'http://tieba.baidu.com/f?kw=%E7%9F%B3%E5%AE%B6%E5%BA%84%E9%93%81%E9%81%93%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
childbaseurl = 'http://tieba.baidu.com'
count = 0
endnum = 100
text = ''
while count <= endnum:
    text = text + bs4tool.geturls(baseurl, count)  # 获取链接
    count = count + 50
    urls = text.split('\n')
    for url in urls:
        filename = url.split("\t")[0].replace('/', '') + '_' + url.split('\t')[1]
        filename = filename.replace('?', '').replace('=', '')  # 设置存储文件名
        url = childbaseurl + url.split("\t")[0]  # 帖子链接
        print(url + ' -> start download ')
        text = bs4tool.gettext(url)
        save_file.SaveFile(text, 'tiezi/' + filename + '.html').save()
