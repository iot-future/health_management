from flask import *
from config import *
from control import openLight, closeLight, openMotor, closeMotor
import math
import json
from flask_cors import CORS
import datetime

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)


@app.route('/test', methods=['GET', 'POST'])
def test():
    db = SQLManager()
    citys = db.get_list('select * from environment ')
    db.close()
    return citys


@app.route('/openLight', methods=['GET', 'POST'])
def open_Light():
    openLight()
    return "successful"


@app.route('/closeLight', methods=['GET', 'POST'])
def close_Light():
    closeLight()
    return "successful"

@app.route('/closeMotor', methods=['GET', 'POST'])
def close_Motor():
    closeMotor()
    return "successful"

@app.route('/openMotor', methods=['GET', 'POST'])
def open_Motor():
    openMotor()
    return "successful"

@app.route('/askDataEnvironment', methods=['GET', 'POST'])
def askDataEnvironment():
    db = SQLManager()
    data = db.get_list('select time,Temperature,Humidity,Luminance,MQ2 from environment')
    data = data[len(data) - 12:len(data)]
    json_data = json.dumps(data, ensure_ascii=False)
    print(json_data)
    return json_data

@app.route('/askDataMax', methods=['GET', 'POST'])
def askDataMax():
    db = SQLManager()
    data = db.get_list('select time,SpO2 from SpO2')
    data = data[len(data) - 12:len(data)]
    json_data = json.dumps(data, ensure_ascii=False)
    print(json_data)
    return json_data
if __name__ == "__main__":
    print(askDataEnvironment())
    app.run(debug=True)

