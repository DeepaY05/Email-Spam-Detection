from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email = request.form['email']

    data = vectorizer.transform([email])
    prediction = model.predict(data)[0]

    result = "Spam" if prediction == 1 else "Not Spam"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)