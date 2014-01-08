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
        myline=re.compile(r"group_name=[^\&service]+").search(line)
        if myline is None:
            continue
        else:
            groupline=myline.group().replace("group_name=",'')
            logdict.setdefault(groupline, []).append(1)

    for groupline in logdict:
        testsort=sum(logdict[groupline])
        sortdict.setdefault(groupline, testsort)
    overdict=sorted(sortdict.iteritems(), key=itemgetter(1), reverse=True)
    
    for sortline, sortcounts in overdict:
        print u"产品线：%-30s  \t调用次数：%s" % (sortline.decode('gb2312'), sortcounts)


