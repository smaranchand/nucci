#!/usr/bin/python3
import argparse
import os
import re
import select
import sys
import subprocess
import pymongo
import yaml

print('''
███    ██    ██    ██     ██████     ██████    ██
████   ██    ██    ██    ██         ██         ██
██ ██  ██    ██    ██    ██         ██         ██
██  ██ ██    ██    ██    ██         ██         ██
██   ████     ██████      ██████     ██████    ██
Developed by: @smaranchand & @yunishshrestha2
''')
dir_path = os.path.expanduser('~/.nucci')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_path = os.path.join(dir_path, 'config.yaml')
if not os.path.exists(file_path):
    with open(file_path, 'a') as f:
        pass
def read_config_file():
    try:
        with open(file_path, "r") as yamlfile:
            config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        myclient = pymongo.MongoClient(config_data['Config']['MONGO_URI'])
        return config_data
    except Exception as e:
        return (e)
def write_config_file(data):
    try:
        with open(file_path, 'w') as yamlfile:
            data1 = yaml.dump(data, yamlfile)
            print("Configuration saved successfully")
    except Exception as e:
        print(f"An error occurred while saving the configuration: {e}")
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
        config_data ={}
        config_data.setdefault('Config', {})['MONGO_URI'] = input('Enter Mongo URI: ')
        config_data.get('Config', {})['DATABASE_NAME'] = input('Enter Database Name: ')
        write_config_file(config_data)
    elif args.webserver:
        script_path = os.path.abspath(os.path.dirname(__file__))
        fullpath=os.path.join(script_path, 'webapp/webapp.py')
        process = subprocess.run(["python3", fullpath])
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
                date, time, vulnerability, scope, severity, endpoint = " ".join(arr[:6]).split()
                data = {"date": "{}".format(date), "time": "{}".format(time), "vulnerability": "{}".format(vulnerability),"scope": "{}".format(scope), "severity": "{}".format(severity), "endpoint": "{}".format(endpoint)}
                x = mycol.insert_one(data)
                print("[+] Results migrated to database.[+]")
    else:
        print("No output data detected.")
if __name__ == '__main__':
    main()