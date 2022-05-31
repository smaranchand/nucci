from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask import make_response
from pymongo import MongoClient
import pdfkit

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
    vulnsraw=mongo.db.nuclei_results.find()
    return render_template('vulnerabilities.html',vulns=vulnsraw)

@app.route('/report')
def index():
    name = "Nuc-Gui"
    html = render_template(
        "report_template.html",
        name=name)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=report.pdf"
    return response

if __name__ == '__main__':
   app.run(debug=True)