import random

class DummyProductClassifier:
    def __init__(self):
        self.categories = ["shoes", "bags", "electronics", "clothing", "groceries"]
    def predict(self, image_data):
        return random.choice(self.categories), round(random.uniform(0.7, 0.99), 2)

class DummyFaceRecognizer:
    def __init__(self):
        self.db = {
            "customer_001": {"name": "Alice Smith", "status": "VIP"},
            "customer_002": {"name": "Bob Johnson", "status": "Regular"}
        }
        self.customer_ids = list(self.db.keys())
    def recognize(self, image_data):
        if random.random() > 0.3:
            return self.db[random.choice(self.customer_ids)]
        return {"name": "Unknown", "status": "Unrecognized"}

class CVService:
    def __init__(self):
        # Using dummy models directly to avoid pickle class scoping issues
        self.product_model = DummyProductClassifier()
        self.face_model = DummyFaceRecognizer()

    def recognize_face(self, image_bytes: bytes):
        if not self.face_model:
            return {"face_detected": False, "status": "Model Offline"}
        
        result = self.face_model.recognize(image_bytes)
        
        if result["name"] == "Unknown":
            return {
                "face_detected": True,
                "status": "Unrecognized",
                "name": "Unknown"
            }
        
        return {
            "face_detected": True,
            "customer_id": "CUST_1001",
            "name": result["name"],
            "loyalty_tier": result["status"],
            "status": "Returning Customer",
            "visit_count": random.randint(1, 20),
            "match_confidence": round(random.uniform(0.85, 0.99), 2)
        }

    def classify_product(self, image_bytes: bytes):
        if not self.product_model:
            return {"status": "error", "category": "Unknown", "confidence": 0.0}
            
        category, confidence = self.product_model.predict(image_bytes)
        return {"status": "success", "category": category, "confidence": confidence}

cv_service = CVService()
