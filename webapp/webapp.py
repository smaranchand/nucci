import yaml
import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
config_dir = os.path.expanduser("~/.nucci")
config_file = os.path.join(config_dir, "config.yaml")
with open(config_file, "r") as yamlfile:
    config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
app.config["MONGO_URI"] = config_data['Config']['MONGO_URI']
mongo = PyMongo(app)
@app.route('/')
def home():
    vulnsraw = mongo.db.nuclei_results.find()
    return render_template('home.html', vulns=vulnsraw, now=datetime.utcnow())
if __name__ == '__main__':
    app.run(debug=False)
