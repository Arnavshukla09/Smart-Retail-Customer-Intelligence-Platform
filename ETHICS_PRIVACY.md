# Ethics, Privacy & Bias Considerations

## 1. Consent and Privacy (Face Recognition)
Face recognition in retail poses significant privacy concerns. This platform is designed strictly for **opt-in loyalty programs**.
* **No Raw Image Storage:** The system extracts facial embeddings and immediately discards the raw image.
* **Right to be Forgotten:** Customers can request deletion of their feature embeddings at any time.

## 2. Demographic Bias Mitigation
Facial recognition models can exhibit bias against certain demographics. 
* We use a high confidence threshold to avoid false positives.
* The model is regularly audited against diverse datasets to ensure equitable performance.

## 3. Data Minimization
The NLP and Sentiment models only process anonymized reviews. No PII (Personally Identifiable Information) is stored in the sentiment analysis logs.
