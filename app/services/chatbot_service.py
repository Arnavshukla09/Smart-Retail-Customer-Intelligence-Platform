import pickle
import json
import random
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_DIR = os.path.join(BASE_DIR, "data")

class ChatbotService:
    def __init__(self):
        self.chatbot_model = None
        self.intents_data = None
        self.load_models()

    def load_models(self):
        try:
            with open(os.path.join(MODELS_DIR, 'chatbot_model.pkl'), 'rb') as f:
                self.chatbot_model = pickle.load(f)
                
            with open(os.path.join(DATA_DIR, 'intents.json'), 'r') as f:
                self.intents_data = json.load(f)
        except Exception as e:
            print(f"Error loading chatbot model or intents: {e}")

    def get_reply(self, message: str):
        if not self.chatbot_model or not self.intents_data:
            return {"reply": "Sorry, I am currently offline.", "error": "Model missing"}
            
        try:
            intent_tag = self.chatbot_model.predict([message])[0]
            for intent in self.intents_data['intents']:
                if intent['tag'] == intent_tag:
                    response = random.choice(intent['responses'])
                    return {"reply": response}
                    
            return {"reply": "I'm not sure how to respond to that."}
        except Exception as e:
            return {"error": str(e), "reply": "An error occurred while processing your request."}

chatbot_service = ChatbotService()
