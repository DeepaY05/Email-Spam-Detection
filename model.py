import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset (you can replace with Kaggle dataset later)
data = {
    'text': [
        "Win money now", "Claim your free prize", "Hello how are you",
        "Let's meet tomorrow", "Free lottery offer", "Project meeting update"
    ],
    'label': [1, 1, 0, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

# Model
model = LogisticRegression()
model.fit(X, df['label'])

# Save model
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved!")