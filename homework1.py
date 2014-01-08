#! /usr/bin/env python

import sys
import os

def get_all(filename):
    allfile=open(filename).read()
    return allfile

def get_counts(allfile):
    counts=allfile.count(name)
    return counts

def get_exist(filename):
    exist=os.path.isfile(filename)
    return exist

if __name__ == '__main__':
    if len(sys.argv) == 3:
        filename=sys.argv[1]
        name=sys.argv[2]
        counts=get_all(filename).count(name)
        print 'There are(is) %s %s in the %s' %  (counts, name, filename)
    elif len(sys.argv) == 2:
        filename=sys.argv[1]
        out=get_exist(filename)
        if out == True:
            print get_all(filename)
        elif out == False:
            print '%s is not exist!' % filename
    elif len(sys.argv) == 1:
        print 'please input the filename'
    else: 
        pass
