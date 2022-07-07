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


if __name__ == '__main__':
    app.run(debug=False)
