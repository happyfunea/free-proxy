#!/usr/bin/python
#-*-coding:utf-8-*-
from subprocess import call as beluk
import sys
#MODULE
from modul import proxUK
from modul import rande
from modul import socks
from modul import about
from colorama import Fore, Back, Style
def banner():
    beluk('clear', shell=True)
    auth = Fore.RED+'''┌─┐┬─┐┌─┐┌─┐  ┌─┐┬─┐┌─┐─┐ ┬┬ ┬
├┤ ├┬┘├┤ ├┤   ├─┘├┬┘│ │┌┴┬┘└┬┘
└  ┴└─└─┘└─┘  ┴  ┴└─└─┘┴ └─ ┴'''+Fore.LIGHTMAGENTA_EX+'''
  --proxy UK
  --socks
  --random Prox\n
'''.upper()
    print auth
    print
    raw = raw_input(Fore.LIGHTWHITE_EX+'(L)anjutkan Tools/(T)idak: ')
    if raw == 'T' or raw == 't':
        print '[Exiting]!'
        sys.exit()
    elif raw == 'L' or raw == 'l':
        beluk('clear', shell=True)
        print Fore.YELLOW+'''(1)'''+Fore.LIGHTGREEN_EX+''' :'''+Fore.LIGHTRED_EX+''' proxy UK'''
        print Fore.YELLOW+'(2)'+Fore.LIGHTGREEN_EX+' :'+Fore.LIGHTRED_EX+' socks'
        print Fore.YELLOW+'(3)'+Fore.LIGHTGREEN_EX+' :'+Fore.LIGHTRED_EX+' random proxy'
        print Fore.YELLOW+'(4)'+Fore.LIGHTGREEN_EX+' :'+Fore.LIGHTRED_EX+' About and Exit'
        print Fore.YELLOW+'(5)'+Fore.LIGHTGREEN_EX+' : '+Fore.LIGHTRED_EX+'Exit'
        print
        try:
            pilih = raw_input(Fore.LIGHTWHITE_EX+'(FREE)# ')
        except KeyboardInterrupt:
            print '\nIterupted by users'
            sys.exit()
        if pilih == '1':
            mod = raw_input('Press Enter...')
            kelas = proxUK.socks()
            kelas.start()
            print (Fore.RED+'\nOUTPUT : ProxyUK.txt')
        elif pilih == '2':
            mode = raw_input('Press Enter...')
            kls = socks.sok()
            kls.start()
            print (Fore.RED+'\nOUTPUT : socks.txt')
        elif pilih == '3':
            moder = raw_input('Press Enter...')
            kles = rande.rand()
            kles.thx()
            print (Fore.RED+'OUTPUT : random.txt')
        elif pilih == '4':
            about.nama()
        elif pilih == '5':
            print Fore.RED+'[Exiting]!';sys.exit()
        else:
            pass
if __name__=='__main__':
    banner()