# Smart Retail & Customer Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.7%2B-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.24%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

An end-to-end, production-style **AI-Powered Smart Retail & Customer Intelligence Platform**. This platform unifies Computer Vision, Natural Language Processing, and automated conversational assistants into a single microservices architecture with a FastAPI REST API gateway and an interactive Streamlit Web Analytics Dashboard.

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [System Architecture](#-system-architecture)
- [Directory Structure](#-directory-structure)
- [Installation & Quick Start](#-installation--quick-start)
- [Docker Deployment](#-docker-deployment)
- [Ethics, Privacy & Bias Considerations](#-ethics-privacy--bias-considerations)
- [Documentation & Final Report](#-documentation--final-report)

## 🎯 Project Overview
Developed for the **MPOnline Advanced Software Engineering Internship Program (AI3 - Batch 6B)**, this project provides a modern brick-and-mortar retail store with seamless automation and intelligent analytics to deliver high-touch customer experiences. 

**Streamlit's Role:** We utilize **Streamlit** as the Presentation Tier to provide a rapid, interactive, and visually premium executive dashboard. Streamlit allows evaluators and end-users to interact with the underlying Computer Vision and NLP models from a unified web interface without writing complex frontend JavaScript.

This platform provides:
1. **Returning Customer Recognition & Visit Logging**: Uses OpenCV facial detection and feature vector embeddings to check in consenting VIP/returning customers and track loyalty visits.
2. **Product Image Classification**: Automatically scans and classifies retail products into core categories with confidence scoring.
3. **Review & Feedback Sentiment Analysis**: Preprocesses customer text reviews and classifies sentiment (*Positive, Negative, Neutral*) using TF-IDF vectorization and machine learning models.
4. **Automated FAQ Chatbot**: A hybrid conversational bot combining exact rule-based pattern matching with an ML intent classifier fallback.
5. **Unified REST API Gateway & Dashboard**: Exposes all models behind a production FastAPI service with OpenAPI/Swagger documentation (`/docs`) and an interactive Streamlit analytics hub.

## 🏗️ System Architecture
The platform adheres strictly to a modular 3-Tier Architecture design pattern:
1. **Presentation Tier:** A custom Streamlit single-page application presents an interactive executive experience.
2. **API Gateway Layer:** FastAPI provides high-performance asynchronous endpoints (`/recognize-face`, `/analyze-sentiment`, `/chatbot`, `/classify-product`).
3. **Model Inference Layer:** Scikit-learn and OpenCV pipelines serialized via `pickle` provide real-time predictive capabilities.

## 📁 Directory Structure
```
smart-retail-ai/
├── app/
│   ├── main.py                     # FastAPI entrypoint with CORS & Swagger docs
│   ├── schemas.py                  # Pydantic models for request/response validation
│   ├── routers/                    # API route definitions
│   └── services/                   # Business logic and ML model inference
├── models/                         # Serialized model artifacts (.pkl files)
├── data/                           # Datasets (e.g., intents.json)
├── tests/                          # Automated Pytest suite
├── scripts/                        # Model training & serialization script
├── dashboard.py                    # Streamlit Web Application
├── ETHICS_PRIVACY.md               # Ethics, privacy & bias documentation
├── Dockerfile                      # Production Docker container setup
├── requirements.txt                # Python dependencies
└── README.md                       # GitHub documentation
```

## 🚀 Installation & Quick Start
### 1. Setup Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
pip install -r requirements.txt
```

### 2. Build Models
```bash
python scripts/build_models.py
```

### 3. Run FastAPI Backend
```bash
uvicorn app.main:app --reload --port 8000
```
API Docs: http://localhost:8000/docs

### 4. Run Streamlit Dashboard
```bash
streamlit run dashboard.py
```
Dashboard: http://localhost:8501

## 🐳 Docker Deployment
```bash
docker build -t smart-retail-platform .
docker run -d -p 8000:8000 -p 8501:8501 --name smart_retail smart-retail-platform
```

## 🔒 Ethics, Privacy & Bias Considerations
- Explicit Consent: Face recognition is strictly opt-in for customer loyalty rewards.
- No Raw Image Storage: The system extracts feature embeddings and immediately discards raw image bytes.
- Demographic Bias Mitigation: Models use conservative confidence thresholds to prevent false positives across diverse groups.

## 📄 Documentation & Final Report
The official academic project report is organized within the `docs/` folder in both PDF and DOCX formats:
- **`docs/Arnav_Shukla_IN26012832_AIML_Program_Internship_AI3_Batch_6B.pdf`**
- **`docs/Arnav_Shukla_IN26012832_AIML_Program_Internship_AI3_Batch_6B.docx`**

These documents detail the complete design, implementation, and quality assurance evaluation of the AI-Powered Smart Retail & Customer Intelligence Platform for MPOnline.
