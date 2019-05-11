from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/data')
def get_data():
    file = r"api.log"
    data_list = []
    with open(file, "r") as f:
        for line in f.readlines():
            newline = (line.replace("\n","").split(","))
            data = []
            data.append(int(newline[0]))
            data.append(int(newline[1]))
            data_list.append(data)
    return jsonify(data_list)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
