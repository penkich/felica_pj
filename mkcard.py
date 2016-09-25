#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 会員カードを作成するテスト（CUI）
# by penkich 2016-08-30
# データベースは、mysql（同一マシン）を使用
# 
import nfc
import re
import mysql.connector
import time

def getid(tag):
    global id
    a = '%s' % tag
    id = re.findall("ID=([0-9A-F]*)",a)[0]

connect = mysql.connector.connect(user='root',password='password',host='127.0.0.1',database='fablab_kitakagaya',charset='utf8')
cursor = connect.cursor()

print "新規に登録するカードをかざして下さい。"
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': getid})
new_id = id
sql = "select count(id) from kaiin where id = '%s'" % new_id
cursor.execute(sql)
if cursor.fetchone()[0] != 0:
    print "既に登録されています"
    exit()
print "番頭さんのカードをかざして下さい。"
time.sleep(2)
clf.connect(rdwr={'on-connect': getid})
banto_id = id
sql = "select count(id) from kaiin where id = '%s'" % banto_id
cursor.execute(sql)
if cursor.fetchone()[0] == 0:
    print "カード が登録されていません"
    exit()
#for row in rows:
#    print row
#
while(True):
    sei = raw_input('姓:')
    mei = raw_input('名:')
    mail = raw_input('メール:')
    penname = raw_input('ペンネーム:')
    inputdata = [new_id,sei,mei,mail,penname]
    #print inputdata
    print ""
    print "ご確認ください"
    print "姓:",sei
    print "名:",mei
    print "メール:",mail
    print "ペンネーム:",penname
    true_chk = raw_input('OK?:(y/n)')
    if true_chk is 'y':
        break

#cursor.execute('insert into kaiin (id,sei,mei,mail,penname) values (%s,%s,%s,%s,%s)',(new_id,sei,mei,mail,penname))
#connect.commit()
##cursor.close()

##cursor = connect.cursor()

cursor.execute('select * from kaiin')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connect.close()

print id
