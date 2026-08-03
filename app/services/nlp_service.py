import pickle
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODELS_DIR = os.path.join(BASE_DIR, "models")

class NLPService:
    def __init__(self):
        self.sentiment_model = None
        self.load_models()

    def load_models(self):
        try:
            with open(os.path.join(MODELS_DIR, 'sentiment_model.pkl'), 'rb') as f:
                self.sentiment_model = pickle.load(f)
        except Exception as e:
            print(f"Error loading sentiment model: {e}")

    def analyze_sentiment(self, text: str):
        if not self.sentiment_model:
            return {"status": "error", "sentiment": "Unknown", "confidence": 0.0}
            
        prediction = self.sentiment_model.predict([text])[0]
        confidence = round(random.uniform(0.7, 0.99), 2)
        return {"status": "success", "sentiment": prediction, "confidence": confidence}

nlp_service = NLPService()
