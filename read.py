#!/usr/bin/python3
#from contextlib import nullcontext
import re
import sys
import select
import yaml
#from turtle import done
import pymongo
print('''
███    ██ ██    ██  ██████        ██████  ██    ██ ██
████   ██ ██    ██ ██            ██       ██    ██ ██
██ ██  ██ ██    ██ ██      █████ ██   ███ ██    ██ ██
██  ██ ██ ██    ██ ██            ██    ██ ██    ██ ██
██   ████  ██████   ██████        ██████   ██████  ██

Developed by:
''')

if select.select([sys.stdin, ], [], [], 0.0)[0]:
    with open("config.yaml", "r") as yamlfile:
        config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)

    myclient = pymongo.MongoClient(config_data['Config']['MONGO_URI'])
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
else:
    print("No output data detected.")