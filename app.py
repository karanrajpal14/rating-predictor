from flask import Flask, jsonify, render_template, request, jsonify
from flask_cors import CORS
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle

app = Flask(__name__)
CORS(app)

model_path = "trained_model/model.pkl"
model_present = False
model = None

vocab_path = "trained_model/vocab.pkl"
vocab_present = False
vocabulary = None

if os.path.isfile(model_path):
    model_present = True
    model = pickle.load(open(model_path, "rb"))
    print("Model present and loaded")

if os.path.isfile(vocab_path):
    vocab_present = True
    vocabulary = pickle.load(open(vocab_path, "rb"))
    print("Vocabulary present and loaded")

@app.route("/", methods=["GET", "POST"])
def index():
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
        if review == "good":
            rating = 7
        else:
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