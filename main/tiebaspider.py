# -*- coding=utf-8 -*-
# author__ = 'nuagevoler'

import main.bs4tool as bs4tool
import main.savefile as save_file
import threading
import time

base_url = 'http://tieba.baidu.com/f?kw=%E7%9F%B3%E5%AE%B6%E5%BA%84%E9%93%81%E9%81%93%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
child_baseurl = 'http://tieba.baidu.com'
count = 0
end_num = 100
text = ''


class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()  # 注意：一定要显式的调用父类的初始化函数。
        self.arg = arg

    def run(self):  # 定义每个线程要运行的函数
        # time.sleep(1)
        url = self.arg
        filename = url.split("\t")[0].replace('/', '') + '_' + url.split('\t')[1]
        filename = filename.replace('?', '').replace('=', '')  # 设置存储文件名
        url = child_baseurl + url.split("\t")[0]  # 帖子链接
        print(url + ' -> start download ')
        text = bs4tool.gettext(url)
        save_file.SaveFile(text, '../tiezi/' + filename + '.html').save()

# for i in range(4):
#     t = MyThread(i)
#     t.start()

while count <= end_num:
    text = text + bs4tool.geturls(base_url, count)  # 获取链接
    count = count + 50
    urls = text.split('\n')
    for url in urls:
        t = MyThread(url)
        t.start()
