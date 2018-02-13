from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ping", methods=['GET'])
def ping():
    return "Service is Healthy"


@app.route('/summary', methods=['GET'])
def get_summary():
    data = [{
        'id': 1,
        'category': 'merge request'
    }]

    return jsonify(data)
