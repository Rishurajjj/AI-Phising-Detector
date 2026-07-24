# 🛡️ AI Phishing Email Detector

> A machine learning-powered web application that detects phishing emails using Natural Language Processing (NLP). The application is built with Python and Flask and deployed on AWS EC2 using Gunicorn and Nginx for production-ready hosting.

---

## 🚀 Live Demo

🌐 **Live Application:**  
http://15.135.47.153

---

## 📖 Overview

Phishing emails are one of the most common cyber threats used to steal sensitive information such as passwords, banking credentials, and personal data. Identifying these emails manually can be difficult, especially when they closely resemble legitimate messages.

This project provides a simple web interface where users can paste the content of an email and instantly receive a prediction indicating whether the email is **Safe** or **Phishing**.

The application uses Natural Language Processing (NLP) for text preprocessing and TF-IDF Vectorization to convert email text into numerical features before making predictions with a trained Machine Learning model.

Apart from the machine learning implementation, the project also demonstrates end-to-end deployment on AWS EC2 using Gunicorn, Nginx, and Systemd.

---

## ✨ Features

- Detects phishing emails in real time
- Machine Learning-based classification
- NLP-based text preprocessing
- TF-IDF feature extraction
- Clean and responsive user interface
- Fast prediction with Flask backend
- Production-ready deployment on AWS EC2
- Gunicorn and Nginx configuration
- Automatic application startup using Systemd

---

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib

### Deployment
- AWS EC2 (Ubuntu)
- Gunicorn
- Nginx
- Systemd
- Git
- GitHub

---

## 📂 Project Structure

```text
AI-Phishing-Email-Detector/
│
├── app.py
├── predictor.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Rishurajj1/AI-Phising-Detector.git
```

### Move to the project directory

```bash
cd AI-Phising-Detector
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. The user enters the content of an email.
2. The email text is cleaned and preprocessed.
3. TF-IDF Vectorizer converts the text into numerical features.
4. The trained Machine Learning model predicts whether the email is Safe or Phishing.
5. The prediction is displayed instantly through the web interface.

---

## ☁️ Deployment

The application is deployed on an Ubuntu-based AWS EC2 instance.

The deployment includes:

- Gunicorn as the WSGI application server
- Nginx as a reverse proxy
- Systemd service for automatic startup
- Elastic IP for public accessibility

This setup allows the application to remain available even after terminal sessions are closed or the server is restarted, making it suitable for production deployment.

---

## 📸 Screenshots

> Screenshots will be added in a future update.

---

## 📌 Future Enhancements

- Improve prediction accuracy with advanced ML models
- Deep Learning-based phishing detection
- Email attachment scanning
- User authentication
- Dashboard for prediction history
- HTTPS support using SSL
- Custom domain integration

---

## 👨‍💻 Author

**Rishu Raj**

B.Tech – Computer Science & Engineering (Cyber Security)

GitHub: https://github.com/Rishurajj1

---

## 📄 License

This project is intended for educational and learning purposes.

---

⭐ If you found this project useful, consider giving it a star.
