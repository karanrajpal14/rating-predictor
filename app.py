from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"project": "Review Rating Predictor", "class": "CSE 5334 002", "course": "Data Mining"})

if __name__ == '__main__':
    app.run(debug=True)