import joblib

model = joblib.load("models/rf_model.pkl")
vectorizer = joblib.load("models/tfidf.pkl")

from feature_engineering import clean_text

def predict_email(email):

    cleaned = clean_text(email)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    confidence = round(max(probability) * 100,2)

    return prediction, confidence