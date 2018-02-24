from flask import Flask, jsonify

from entry.services.entry_service import EntryService

app = Flask(__name__)


@app.route("/ping", methods=['GET'])
def ping():
    return "Service is Healthy"


@app.route('/entry', methods=['GET'])
def get_entries():
    return jsonify(EntryService.get_entries())
