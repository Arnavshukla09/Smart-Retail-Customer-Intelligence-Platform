import streamlit as st
import requests

st.set_page_config(page_title="Smart Retail Dashboard", layout="wide", page_icon="🛍️")

st.title("🛍️ Smart Retail & Customer Intelligence Dashboard")
st.markdown("### Executive Analytics Overview")

try:
    res = requests.get("http://127.0.0.1:8000/dashboard/stats")
    if res.status_code == 200:
        stats = res.json()
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Daily Visits", stats.get("daily_visits", 0))
        col2.metric("Returning VIPs", stats.get("returning_customers", 0))
        col3.metric("Avg Sentiment", f"{stats.get('sentiment_score', 0)}/10")
        col4.metric("Top Category", stats.get("top_category", "N/A").capitalize())
except:
    st.error("Could not connect to the backend API. Is it running on port 8000?")

st.markdown("---")
st.header("🤖 Test AI Services")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("1. Customer Chatbot")
    user_msg = st.text_input("Ask the support bot:")
    if st.button("Send"):
        try:
            res = requests.post("http://127.0.0.1:8000/chatbot", json={"message": user_msg})
            if res.status_code == 200:
                st.info(f"**Bot:** {res.json().get('reply')}")
        except:
            st.error("Error communicating with Chatbot API.")
            
with col_b:
    st.subheader("2. Sentiment Analysis")
    review_text = st.text_area("Analyze a customer review:")
    if st.button("Analyze"):
        try:
            res = requests.post("http://127.0.0.1:8000/analyze-sentiment", json={"text": review_text})
            if res.status_code == 200:
                data = res.json()
                st.success(f"Sentiment: **{data.get('sentiment')}** (Confidence: {data.get('confidence')})")
        except:
            st.error("Error communicating with NLP API.")

st.markdown("---")
st.subheader("📷 Computer Vision Test")
uploaded_file = st.file_uploader("Upload an image for Product Classification or Face Recognition", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width=300)
    
    col_c, col_d = st.columns(2)
    with col_c:
        if st.button("Recognize Customer"):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                res = requests.post("http://127.0.0.1:8000/recognize-face", files=files)
                st.json(res.json())
            except Exception as e:
                st.error(f"API Error: {e}")
                
    with col_d:
        if st.button("Classify Product"):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                res = requests.post("http://127.0.0.1:8000/classify-product", files=files)
                st.json(res.json())
            except Exception as e:
                st.error(f"API Error: {e}")
