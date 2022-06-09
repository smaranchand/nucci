#!/usr/bin/python3
# from contextlib import nullcontext
import re
import select
import sys
# from turtle import done
import pymongo
from pymongo import MongoClient
import yaml

print('''


███    ██    ██    ██     ██████     ██████    ██
████   ██    ██    ██    ██         ██         ██
██ ██  ██    ██    ██    ██         ██         ██
██  ██ ██    ██    ██    ██         ██         ██
██   ████     ██████      ██████     ██████    ██

Developed by: Smaran & Yunish
''')
try:
    with open("config.yaml", "r") as yamlfile:
        config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    myclient = pymongo.MongoClient(config_data['Config']['MONGO_URI'])
except Exception as e:
    print(e)
if select.select([sys.stdin,], [], [], 0.0)[0]:
    rawdata = sys.stdin.read()
    regexmatch = re.compile(r'\x1b[^m]*m')
    results = regexmatch.sub('', rawdata)
    new = (results.translate(results.maketrans({'[': '', ']': ''})))
    for data in new.splitlines():
        arr = data.split()
        date = (arr[0])
        time = (arr[1])
        vulnerability = (arr[2])
        scope = (arr[3])
        severity = (arr[4])
        endpoint = (arr[5])
        mydb = pymongo.MongoClient(config_data['Config']['DATABASE_NAME'])
        mycol = mydb["nuclei_results"]
        data = {"date": "" + date, "time": "" + time, "vulnerability": "" + vulnerability, "scope": "" + scope,"severity": "" + severity, "endpoint": "" + endpoint}
        x = mycol.insert_one(data)
        print("[+] Results migrated to database.[+]")
else:
    print("No output data detected.")
