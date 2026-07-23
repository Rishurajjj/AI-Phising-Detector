from flask import Flask, render_template, request
from explain import explain_email
from predictor import predict_email

app = Flask(__name__)

print("Flask app is running...")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    email = request.form["email"]

    prediction, confidence = predict_email(email)
    if prediction == 1:

        prediction_text = "🚨 PHISHING EMAIL DETECTED"
        color = "red"
        risk = "High Risk"
    else:

        prediction_text = "✅ SAFE EMAIL"
        color = "green"
        risk = "Low Risk"


    threat_score, reasons = explain_email(email)

    return render_template(
        "index.html",
        prediction=prediction_text,
        confidence=confidence,
        threat_score=threat_score,
        reasons=reasons,
        color=color,
        risk=risk
    )

if __name__ == "__main__":
    app.run(debug=True) 
    

    