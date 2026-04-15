📧 Email Spam Detection using Machine Learning

🔍 Overview

This project is a Machine Learning-based web application that classifies emails as **Spam** or **Not Spam**. It uses Natural Language Processing (NLP) techniques along with a trained model to analyze email content and predict its category.

🚀 Features

* Real-time email classification
* Clean and simple web interface using Flask
* Uses trained ML model for prediction
* Fast and lightweight implementation

🧠 Tech Stack

* Python
* Flask
* Scikit-learn
* NLTK
* HTML/CSS

📂 Project Structure

Practical_9_Email_Spam_Detection/
│
├── app.py                # Flask application
├── model.py              # Model training logic
├── spam_model.pkl        # Trained ML model
├── vectorizer.pkl        # TF-IDF vectorizer
│
├── templates/
│   └── index.html        # Frontend UI
│
└── static/               # CSS files (if any)

⚙️ How It Works

1. Input email text from user
2. Text is preprocessed using NLP techniques
3. Converted into numerical format using TF-IDF vectorizer
4. Model predicts whether it is Spam or Not Spam
5. Result is displayed on the web interface

▶️ How to Run the Project

1. Clone the repository

git clone https://github.com/Deepay05/Email-Spam-Detection.git

2. Navigate to project folder

cd Email-Spam-Detection

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

5. Open in browser

http://127.0.0.1:5000

📊 Model Details

* Algorithm Used: Logistic Regression / Naive Bayes
* Feature Extraction: TF-IDF Vectorization
* Text Preprocessing: Lowercasing, removing special characters, stopwords removal

📌 Example

Input:

Congratulations! You have won a free lottery ticket.

Output:

Spam

🎯 Future Improvements

* Add accuracy metrics and model evaluation
* Improve UI/UX design
* Deploy application online
* Use advanced models like BERT

👨‍💻 Author

Deepay05

⭐ Acknowledgment

This project was developed as part of a Machine Learning practical assignment.
