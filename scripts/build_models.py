import json
import pickle
import os
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(MODELS_DIR, exist_ok=True)

print("Building NLP Models...")
reviews = ["Great store!", "Terrible service.", "Okay products.", "Fast delivery.", "Never buy here again.", "Fine experience."]
labels = ["Positive", "Negative", "Neutral", "Positive", "Negative", "Neutral"]
sentiment_pipeline = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')), ('clf', LogisticRegression(random_state=42))])
sentiment_pipeline.fit(reviews, labels)

with open(os.path.join(MODELS_DIR, 'sentiment_model.pkl'), 'wb') as f:
    pickle.dump(sentiment_pipeline, f)
print("Sentiment Analysis Model saved.")

with open(os.path.join(DATA_DIR, 'intents.json'), 'r') as f:
    intents_data = json.load(f)

patterns, tags = [], []
for intent in intents_data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])

chatbot_pipeline = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')), ('clf', LogisticRegression(random_state=42))])
chatbot_pipeline.fit(patterns, tags)

with open(os.path.join(MODELS_DIR, 'chatbot_model.pkl'), 'wb') as f:
    pickle.dump(chatbot_pipeline, f)
print("Chatbot Intent Model saved.")

print("Mocking CV Models...")
class DummyProductClassifier:
    def __init__(self): self.categories = ["shoes", "bags", "electronics", "clothing", "groceries"]
    def predict(self, image_data): return random.choice(self.categories), round(random.uniform(0.7, 0.99), 2)

with open(os.path.join(MODELS_DIR, 'product_classifier.pkl'), 'wb') as f:
    pickle.dump(DummyProductClassifier(), f)

face_db = {"customer_001": {"name": "Alice Smith", "status": "VIP"}, "customer_002": {"name": "Bob Johnson", "status": "Regular"}}
class DummyFaceRecognizer:
    def __init__(self, db): self.db = db; self.customer_ids = list(self.db.keys())
    def recognize(self, image_data):
        if random.random() > 0.3: return self.db[random.choice(self.customer_ids)]
        return {"name": "Unknown", "status": "Unrecognized"}

with open(os.path.join(MODELS_DIR, 'face_db.pkl'), 'wb') as f:
    pickle.dump(DummyFaceRecognizer(face_db), f)
print("CV Models mocked successfully.")
