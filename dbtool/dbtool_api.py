#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: qiantu
#qq 261767353
# !/usr/bin/env python

# from django.db import connection
import MySQLdb as mdb
from dbtool.models import Dblist

exec_db_host="192.168.1.175"
exec_db_user="zzjr"
exec_db_password='zzjr#2015'
exec_db_name='zzjr_server'


cmd='''
  update
zzjr_server.member_money_record m,
zzjr_server.trade_order t
SET
m.stream_sn = concat( 'UN', m.stream_sn )
where
m.stream_sn = t.order_sn
and t.trade_type = 3
and t.status = 1
and t.bank_sync_status = 4
and t.gmt_create BETWEEN '2017-04-13 13:00:11' AND '2017-04-14 09:00:25';
            

'''

def exec_db(db_name,cmd):
    con = mdb.connect(exec_db_host, exec_db_user, exec_db_password, exec_db_name, charset='utf8')
    cur = con.cursor()
    cur.execute(cmd)
    cur.close()
    mod_rows = cur.rowcount
    print mod_rows
    con.commit()
    return mod_rows

exec_db('zzjr_bank',cmd)



def db_list(db_role):
    dblist=Dblist.objects.filter(db_role=db_role)

    return dblist