# -*- coding=utf-8 -*-

# 存到本地
class SaveFile:
    def __init__(self,htmlcontent,filename):
        self.content = htmlcontent
        self.filename = filename
    def save(self):
        output = open(self.filename,"w+",encoding= 'utf8')
        output.write(self.content)
        output.close()

#SaveFile("test,中文，你好","save.txt").save()
