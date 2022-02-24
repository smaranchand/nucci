from flask import Flask, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
app = Flask(__name__)

#Moving to the cloud database
#app.config["MONGO_URI"] = "mongodb://localhost:27017/scanresults"
app.config["MONGO_URI"] = "mongodb+srv://root:localhost123@nuc-gui-db.zolos.mongodb.net/scanresults?retryWrites=true&w=majority"
#db = client.test
mongo = PyMongo(app)


@app.route('/')
def home():
    vulnsraw=mongo.db.nuclei_results.find()
    return render_template('home.html', vulns=vulnsraw)



@app.route('/connect')
def connect():
    return render_template('connect.html')

@app.route('/vulnerabilities')
def vulnerabilities():
    return render_template('vulnerabilities.html')

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
   app.run(debug=True)