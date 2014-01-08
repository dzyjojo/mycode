#!/usr/bin/env python
#coding:utf-8
import urllib
import urllib2
import sys

def post():
        IP=sys.argv[1]
        CMD=sys.argv[2]
        url='https://xxx.sina.com/xxx.xxx'
        argument={ 'user':'zhiyang',
                   'method':'sync',
                   'output':'text',
                   'ignore_error':'true',
                   'key':'d41d8cd98f00b204e9800998ecf8427e',
                   'timeout':'5',
                   'ip':IP,
                   'cmd':CMD
                }
        data = urllib.urlencode(argument)
        response = urllib2.urlopen(url, data)
        print response.read()


if __name__ == '__main__':
        if len(sys.argv) == 1:
                print """
                      Usage ./channel.py '$IP' '$CMD'
                      """
        else:
                post()

