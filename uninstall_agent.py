#!/usr/bin/env python
import urllib2
import json 

def get_all():
    info = open('/home/zhiyang/monitor/installing.txt', 'r')
    all_agents = info.readlines()
    return all_agents

def get_installed():
    response = urllib2.urlopen('http://xxx.sina.com.cn/configuration/host/agents/')
    info = response.read()
    installed_agents =  json.loads(info)['data']['list']
    return installed_agents


if __name__ == "__main__":
    installed = get_installed()
    all = get_all()
    print len(installed), len(all)
    for i in all:
        i = i.replace('\n', '')
        if i in installed:
            continue
        else:
            print i
