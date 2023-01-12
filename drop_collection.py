import os
import yaml
import pymongo

dir_path = os.path.expanduser('~/.nucci')
file_path = os.path.join(dir_path, 'config.yaml')
with open(file_path, "r") as yamlfile:
    config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
try:
    myclient = pymongo.MongoClient(config_data["Config"]["MONGO_URI"])
    mydb = myclient[config_data["Config"]["DATABASE_NAME"]]
    collection_name = "nuclei_results"
    if collection_name in mydb.list_collection_names():
        confirm = input(f"Are you sure you want to drop the {collection_name} collection? (y/n)")
        if confirm.lower() == "y":
            mycol = mydb[collection_name]
            mycol.drop()
except Exception as e:
    print(f"An error occurred: {e}")
