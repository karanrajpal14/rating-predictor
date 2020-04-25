from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"hello": "world", "from": "index"})

@app.route("/foo")
def foo():
    return jsonify({"hello": "world", "from": "foo"})

if __name__ == '__main__':
    app.run(debug=True)