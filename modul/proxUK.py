#!/usr/bin/python
#-*-coding:utf-8-*-
import requests
import re
class socks:
    url = 'https://www.socks-proxy.net/'
    co = 0
    def __init__(self):
        self.file = open('ProxyUK.txt', 'w')
        self.get = requests.get(socks.url).text
    def start(self):
        self.regx = re.findall(r'<td>(.*?)</td>', self.get)
        self.data = [dict(zip(['ip','port','kode','ini lagi apa ya?'],
                              self.regx[i:i+4])) \
                     for i in range(0, len(self.regx), 4)]
        for c in self.data:
            self.file.write(c['ip']+':'+c['port']+'\n')
            socks.co+=1
            print socks.co,': '+c['ip']+':'+c['port']
        self.file.close()
