#!/usr/bin/python
#-*-coding:utf-*-
#FOLLOW MY FACEBOOK:v fb.me/agung3131
import requests, re
class rand:
    url = 'https://free-proxy-list.net/'
    co = 0
    def __init__(self):
        self.filer = open('random.txt', 'w')
        self.get = requests.get(rand.url).text
    def thx(self):
        self.find = re.findall(r'<td>(.*?)</td>', self.get)
        self.data = [dict(zip(['ip','port','kode','agung ganteng tq'],
                              self.find[b:b+4])) \
                     for b in range(0, len(self.find), 4)]
        for y in self.data:
            rand.co+=1
            self.filer.write(y['ip']+':'+y['port']+'\n')
            print rand.co, ': '+y['ip']+':'+y['port']
        self.filer.close()
