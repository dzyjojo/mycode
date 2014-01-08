#!/usr/bin/env python

from elasticsearch import Elasticsearch

def fetch():
    try:
        es = Elasticsearch(hosts=('http://10.13.56.95:9200'))
    except:
        print 'failed to fetch'
    doc = {
        'field': '@timestamp',
        'from' : '2013-12-25T15:55:13.642889',
        'to' : '2013-12-25T20:24:13.418975',
        'size': 100,
#        'sort': {'@timestamp': 'desc'}
        }
    res = es.search(index='sinawatch-alert-2013.12.25', body=doc)
    return res

if __name__ == '__main__':
    print fetch()
