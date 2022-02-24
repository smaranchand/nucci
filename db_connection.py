from pymongo import MongoClient
client = MongoClient("mongodb+srv://root:localhost123@nuc-gui-db.zolos.mongodb.net/scanresults?retryWrites=true&w=majority")
db = client.scanresults
try: db.command("ConnectionStatus")
except Exception as e: print(e)
else: print("You are connected to the database!")
client.close()
