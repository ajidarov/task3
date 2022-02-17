import json
import dicttoxml
from flask import Flask, request

app = Flask(__name__)


@app.route("/result", methods=["POST", "GET"])
def result():
    output = request.get_json()
    obj = json.dumps(output)
    obj = json.loads(obj)
    xml = dicttoxml.dicttoxml(obj)
    return xml


if __name__ == '__main__':
    app.run(debug=True, port=2000)
