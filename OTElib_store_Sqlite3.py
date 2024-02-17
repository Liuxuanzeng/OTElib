#coding:utf-8
# by liuxuanzeng
# 2023-5-7
# oTElib中fasta导入sqlite3    为OTElib.db


import pyfastx
import sqlite3
import sys

fafile = sys.argv[1]
dbfile = fafile + '.db'

OTEfa = pyfastx.Fasta(fafile)
db = sqlite3.connect(dbfile)
cur =db.cursor()
sql = '''CREATE TABLE if not exists OTElib (id text primary key, spname text, class text, familyn text, seq text)'''
cur.execute(sql)
z = 1
for seq in OTEfa:
    rawname = seq.name
    species1 = rawname.split("__")[1]
    speciesname = species1.split("-")[0]
    TEname = rawname.split("#")[1]
    keyname = rawname.split('#')[0]
    keyname = str(z) + '_' + keyname
    z = z + 1
    TEnamelist = TEname.split("/")
    sequence = seq.seq
    if len(TEnamelist) == 2:
        Classn = TEnamelist[0]
        familyn = TEnamelist[1]
        inlist = (keyname, speciesname, Classn, familyn, sequence)
    else:
        Classn = TEnamelist[0]
        inlist = (keyname, speciesname, Classn, None, sequence)
    cur.execute('INSERT INTO OTElib VALUES(?,?,?,?,?)', (inlist[0], inlist[1], inlist[2], inlist[3], inlist[4]))

db.commit()
cur.close()
db.close()


