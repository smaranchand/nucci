#!/usr/bin/python3
import argparse
import os
import re
import sys
import pymongo
import select
import yaml

print('''
███    ██    ██    ██     ██████     ██████    ██
████   ██    ██    ██    ██         ██         ██
██ ██  ██    ██    ██    ██         ██         ██
██  ██ ██    ██    ██    ██         ██         ██
██   ████     ██████      ██████     ██████    ██

Developed by:@smaranchand & Yunish
''')
def read_config_file():
    try:
        with open("config.yaml", "r") as yamlfile:
            config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        return config_data
    except Exception as e:
        print(e)

def write_config_file(data):
    try:
        with open("config.yaml", 'w') as yamlfile:
            data1 = yaml.dump(data, yamlfile)
            print("Configuration saved successfully")
            yamlfile.close()
    except Exception as e:
        print(e)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='Add MongoDB configuration', action='store_true')
    parser.add_argument('--webserver', help='Start the web server', action='store_true')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    if args.config:
        config_data = read_config_file()
        config_data['Config']['MONGO_URI'] = input('Enter Mongo URI: ')
        config_data['Config']['DATABASE_NAME'] = input('Enter Database Name: ')
        write_config_file(config_data)
    elif args.webserver:
        os.system("cd webapp && python3 webapp.py")
    elif select.select([sys.stdin, ], [], [], 0.0)[0]:
        config_data = read_config_file()
        myclient = pymongo.MongoClient(config_data['Config']['MONGO_URI'])
        mydb = myclient[config_data['Config']['DATABASE_NAME']]
        mycol = mydb["nuclei_results"]
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
            data = {"date": "" + date, "time": "" + time, "vulnerability": "" + vulnerability, "scope": "" + scope,
                    "severity": "" + severity, "endpoint": "" + endpoint}
            x = mycol.insert_one(data)
            print("[+] Results migrated to database.[+]")
    else:
        print("No output data detected.")

if __name__ == '__main__':
    main()