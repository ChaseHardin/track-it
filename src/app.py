from flask import Flask, jsonify

from entry.entry_service import Entry

app = Flask(__name__)


@app.route("/ping", methods=['GET'])
def ping():
    return "Service is Healthy"


@app.route('/entry', methods=['GET'])
def get_entries():
    return jsonify(Entry.get_entries())
