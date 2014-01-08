#! /usr/bin/env python

import MySQLdb

try:
        conn=MySQLdb.connect(host='x.x.x.x',user='root',db='CMDB')
        cur=conn.cursor()
        cur.execute('select * from view_all_unit limit 10')
        cur.close()
        conn.close()
except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
