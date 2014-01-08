#!/usr/local/sinawatch_python/bin/python
#-*- coding=utf-8 -*-
import pymongo,sys
 
class MongodbCollect(object):
    '''连接mongodb服务器'''
    def connectMongoDB(self,host,port):
        self.host = host
        self.port = port
        self.stats = {}
        try:
            mongoConnection = pymongo.Connection(self.host,self.port)
            db = mongoConnection.admin
            db.authenticate('', '')
            self.stats = db.command("serverStatus")
            mongoConnection = None
            return self.stats
        except EOFError:
            print 'Notice , Check the Error fix it. '
            sys.exit()
 
    def checkDataInNums(self):
        self.dataDic = {}
        current_connectNum = self.stats["connections"]["current"] - 1 #当前活动连接量,连接到server的当前活跃连接数目
        available_connectNum = self.stats["connections"]["available"] #剩余空闲连接量,剩余的可用连接数目
        activeClientsTotal_connectNum = self.stats["globalLock"]["activeClients"]["total"] #连接到server的当前活动client数目
        activeClientsReaders_connectNum = self.stats["globalLock"]["activeClients"]["readers"] #执行读操作的当前活动client数目
        activeClientsWriters_connectNum = self.stats["globalLock"]["activeClients"]["writers"] #执行写操作的当前活动client数目
        opcounters_insertNum = self.stats["opcounters"]["insert"] #自server实例启动以来总的insert数据量
        opcounters_queryNum = self.stats["opcounters"]["query"] #自server实例启动以来总的query数据量
        opcounters_updateNum = self.stats["opcounters"]["update"] #自server实例最近启动以来总的update数据量
        opcounters_deleteNum = self.stats["opcounters"]["delete"] #自server实例启动以来总的delete数据量
	network_bytesIn = self.stats["network"]["bytesIn"] #发送到数据库的数据总量(bytes)
	network_bytesOut = self.stats["network"]["bytesOut"] #数据库发出的数据总量(bytes)
	network_numRequests= self.stats["network"]["numRequests"] #发送到数据库的请求量
        self.dataDic = {
                   'cc':current_connectNum ,
                   'ac':available_connectNum,
                   'atc':activeClientsTotal_connectNum,
                   'arc':activeClientsReaders_connectNum,
                   'awc':activeClientsWriters_connectNum,
                   'oi':opcounters_insertNum,
                   'oq':opcounters_queryNum,
                   'ou':opcounters_updateNum,
                   'od':opcounters_deleteNum,
		   'ni':network_bytesIn,
		   'no':network_bytesOut,
		   'nr':network_numRequests
                   }
        return self.dataDic
 
    def judgeChoice(self,choice):
        self.choice = choice
        if self.choice == 'cn':
            cc = '%s:%d %s:%d' % ('ac',self.dataDic['ac'],'cc',self.dataDic['cc'])
            return cc
        elif self.choice == 'ac':
            ac = '%s:%d %s:%d %s:%d' % ('atc',self.dataDic['atc'],'arc',self.dataDic['arc'],'awc',self.dataDic['awc'])
            return ac
        elif self.choice == 'co':
            co = '%s:%d %s:%d %s:%d %s:%d' % ('oi',self.dataDic['oi'],'oq',self.dataDic['oq'],'ou',self.dataDic['ou'],'od',self.dataDic['od'])
            return co
	elif self.choice == 'nb':
            nb = '%s:%d %s:%d %s:%d' % ('ni',self.dataDic['ni'],'no',self.dataDic['no'],'nr',self.dataDic['nr'])
	    return nb
	elif self.choice == 'all':
	    all = '%s:%d %s:%d %s:%d %s:%d %s:%d %s:%d %s:%d %s:%d %s:%d %s:%d %s:%d %s:%d' % ('ac',self.dataDic['ac'],'cc',self.dataDic['cc'],'atc',self.dataDic['atc'],'arc',self.dataDic['arc'],'awc',self.dataDic['awc'],'oi',self.dataDic['oi'],'oq',self.dataDic['oq'],'ou',self.dataDic['ou'],'od',self.dataDic['od'],'ni',self.dataDic['ni'],'no',self.dataDic['no'],'nr',self.dataDic['nr'])
	    return all
        else:
            error = 'Please , input the right options like cc|ac|co .'
            return error
if __name__=='__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    choice = sys.argv[3]
    rbt = MongodbCollect()
    rbt.connectMongoDB(host,port)
    rbt.checkDataInNums()
    print rbt.judgeChoice(choice)
