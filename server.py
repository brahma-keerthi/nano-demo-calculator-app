from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World', 200

@app.route("/calculator/add", methods=['POST'])
def add():
    first = request.form.get('first')
    second = request.form.get('second')
    return jsonify( {'result' : int(first) + int(second)} ), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    first = request.form.get('first')
    second = request.form.get('second')
    return jsonify( {'result' : int(first) - int(second)} ), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
