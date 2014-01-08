#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from operator import itemgetter

def get_array(lname):
    content=open(lname, 'r')
    cacheline=content.readlines()
    return cacheline

if __name__ == '__main__':
    logname='/home/zhiyang/study/alterinterface.log'
    logdict={}
    sortdict={}

    for line in get_array(logname):
        myline=re.compile(r"^(\d{1,3}\.){1,3}\d{1,3} ").search(line)
        if myline is None:
            continue
        else:
            ipline=myline.group()
            logdict.setdefault(ipline, []).append(1)

    for ipline in logdict:
        testsort=sum(logdict[ipline])
        sortdict.setdefault(ipline, testsort)
    overdict=sorted(sortdict.iteritems(), key=itemgetter(1), reverse=False)
    
    for sortline, sortcounts in overdict:
        print "ip地址：%-20s 调用次数：%d" % (sortline, sortcounts)



