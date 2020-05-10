from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    errors = []
    results = {}
    form = None
    rating = 0
    form = request.form
    try:
        review = form['review']
        if review == "good":
            rating = 7
        else:
            rating = 1
        results = {"review": review, "rating": rating}
    except:
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again."
        )
    return jsonify({"results": results, "errors": errors, "form": form})

if __name__ == '__main__':
    app.run(debug=True)