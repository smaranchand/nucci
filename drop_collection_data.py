import pymongo
myclient = pymongo.MongoClient("mongodb+srv://root:localhost123@nuc-gui-db.zolos.mongodb.net/scanresults?retryWrites=true&w=majority")
mydb = myclient["scanresults"]
mycol = mydb["nuclei_results"]
mycol.drop()