from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"project": "Review Rating Predictor", "class": "CSE 5334 002", "course": "Data Mining"})

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    errors = []
    results = {}
    form = None
    rating = 0

    if request.method == "POST":
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
    else:
        errors.append("Form submission not recieved. Please make a POST call to the API with your review.")

    return jsonify({"results": results, "errors": errors, "form": form})


if __name__ == '__main__':
    app.run(debug=True)