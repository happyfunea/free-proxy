#!/usr/bin/python
#-*-coding:utf-8-*-
import requests
import re
class sok:
    url = 'https://www.socks-proxy.net/'
    co = 0
    def __init__(self):
        self.filer = open('socks.txt', 'w')
        self.get = requests.get(sok.url).text
    def start(self):
        self.regx = re.findall(r'<td>(.*?)</td>', self.get)
        self.data = [dict(zip(['ip','port','kode','ini lagi apa ya?'],
                              self.regx[i:i+4])) \
                     for i in range(0, len(self.regx), 4)]
        for c in self.data:
            self.filer.write('-->'+c['ip']+':'+c['port']+'\n')
            sok.co+=1
            print sok.co, ':'+'--> '+c['ip']+':'+c['port']
        self.filer.close()