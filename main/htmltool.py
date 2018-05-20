# -*- coding=utf-8 -*-

import urllib.request  

def getcontent(url):
    request = urllib.request.Request(url)  
    response = urllib.request.urlopen(request) 
    data = response.read()
    data = data.decode('utf-8') 
    return data