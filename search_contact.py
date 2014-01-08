#!/usr/bin/env python
import urllib2

#search from erp
#show contact.txt
#xxx@staff.sina.com.cn,xx@staff.sina.com.cn

def get_contact():
    contact=open('/home/zhiyang/monitor/contact.txt', 'r').read()
    return contact

def get_info(mail):
    url='http://ttm.erp.sina.com.cn/api/empinfo.php?email=%s' % mail
    data=urllib2.urlopen(url)
    info=data.read()
    return info

if __name__ == "__main__":
    contact=get_contact()
    people=contact.split(',')
    info_dic={}
    for mail in people:
        info=get_info(mail)
        info=info.decode('gbk').encode('utf8')
        info=info.replace('"', '').replace('{', '').replace('}', '')
        print info
