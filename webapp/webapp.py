from datetime import datetime

import yaml
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
try:
    with open("../config.yaml", "r") as yamlfile:
        config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
except Exception as e:
    print(e)
# Moving to the cloud database
app.config["MONGO_URI"] = config_data['Config']['MONGO_URI']
mongo = PyMongo(app)


@app.route('/')
def home():
    vulnsraw = mongo.db.nuclei_results.find()
    return render_template('home.html', vulns=vulnsraw, now=datetime.utcnow())


# @app.route('/connect')
# def connect():
#     return render_template('connect.html')

# @app.route('/vulnerabilities')
# def vulnerabilities():
#     vulnsraw=mongo.db.nuclei_results.find()
#     return render_template('vulnerabilities.html',vulns=vulnsraw)

# @app.route('/report')
# def index():
#     name = "Nuc-Gui"
#     html = render_template(
#         "report_template.html",
#         name=name)
#     pdf = pdfkit.from_string(html, False)
#     response = make_response(pdf)
#     response.headers["Content-Type"] = "application/pdf"
#     response.headers["Content-Disposition"] = "inline; filename=report.pdf"
#     return response

if __name__ == '__main__':
    app.run(debug=False)
