import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_dashboard_stats():
    response = client.get("/dashboard/stats")
    assert response.status_code == 200
    assert "daily_visits" in response.json()

def test_analyze_sentiment_positive():
    response = client.post("/analyze-sentiment", json={"text": "I love this product!"})
    assert response.status_code == 200
    assert response.json()["status"] in ["success", "error"]

def test_chatbot_rule_matching():
    response = client.post("/chatbot", json={"message": "Hi"})
    assert response.status_code == 200
    assert "reply" in response.json()
