#!/usr/bin/python3
from contextlib import nullcontext
import re
import sys
#from turtle import done
import pymongo
print('''
███    ██ ██    ██  ██████        ██████  ██    ██ ██
████   ██ ██    ██ ██            ██       ██    ██ ██
██ ██  ██ ██    ██ ██      █████ ██   ███ ██    ██ ██
██  ██ ██ ██    ██ ██            ██    ██ ██    ██ ██
██   ████  ██████   ██████        ██████   ██████  ██
''')
myclient = pymongo.MongoClient('mongodb+srv://root:localhost123@nuc-gui-db.zolos.mongodb.net/scanresults?retryWrites=true&w=majority')
rawdata = sys.stdin.read()
regexmatch = re.compile(r'\x1b[^m]*m')
results = regexmatch.sub('', rawdata)
new=(results.translate(results.maketrans({'[': '', ']': ''})))
for data in new.splitlines():
    arr=data.split()
    date=(arr[0])
    time=(arr[1])
    vulnerability=(arr[2])
    scope=(arr[3])
    severity=(arr[4])
    endpoint=(arr[5])
    mydb = myclient["scanresults"]
    mycol = mydb["nuclei_results"]
    data = { "date":""+date , "time":""+time , "vulnerability":""+vulnerability , "scope":""+scope , "severity":""+severity , "endpoint":""+endpoint }
    x = mycol.insert_one(data)
    print("[+] Results migrated to database.[+]")