from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify({"results": "Hellow world!"})

@app.route("/predict", methods=["POST"])
def predict():
    errors = []
    results = {}
    form = None
    rating = 0
    try:
        review = request.json['review']
        model = pickle.load(open("trained_model/model.pkl", "rb"))
        vocabulary = pickle.load(open("trained_model/vocab.pkl", "rb"))
        vectorizer = TfidfVectorizer(vocabulary=vocabulary)
        comment = vectorizer.fit_transform([review])
        rating = round(model.predict(comment)[0])    
        results = {"review": review, "rating": rating, "modelLoaded": model_present, "vocabLoaded": vocab_present}
    except Exception as e:
        print(e)
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again."
        )
    return jsonify({"results": results, "errors": errors})

if __name__ == '__main__':
    app.run(debug=True)