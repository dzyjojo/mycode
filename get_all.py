#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re,sys
from operator import itemgetter

def get_array(lname):
    content=open(lname, 'r')
    cacheline=content.readlines()
    return cacheline

if __name__ == '__main__':
    logname=sys.argv[1]
    logdict={}
    ipdict={}
    sortipdict={}

    for line in get_array(logname):
        myline=re.compile(r"group_name=[^\&service]+").search(line)
        if myline is None:
            continue
        else:
            allline=myline.string
            groupline=myline.group().replace("group_name=",'')
            logdict.setdefault(groupline, []).append(allline)
    for group in logdict.keys():
        iparray=logdict[group]
        testsort=len(iparray)
        iptest="产品线：%s\t%s" % (group.decode('gb2312').encode('utf8'), testsort)
        print iptest
        ipdict={}
        for line in iparray:
            myline=re.compile(r"(\d{1,3}\.){1,3}\d{1,3} ").search(line)
            if myline is None:
                continue
            else:
                ipline=myline.group()
                ipdict.setdefault(ipline, []).append(1)
        sortipdict={}
        for ipline in ipdict:
            ipsort=sum(ipdict[ipline])
            sortipdict.setdefault(ipline, ipsort)
        overipdict=sorted(sortipdict.iteritems(), key=itemgetter(1), reverse=True)
        for sortline, sortcounts in overipdict:
            print "ip地址：%-30s \t调用次数：%d \t%-20s" % (sortline, sortcounts, group.decode('gb2312').encode('utf8'))

