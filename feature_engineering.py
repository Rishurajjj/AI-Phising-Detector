
import re
import string
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):

    text = text.lower()

    text = re.sub(r'http\S+', '', text)

    text = re.sub(r'\d+', '', text)

    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    words = [word for word in words if word not in stop_words]

    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)




def has_url(email):
    pattern = r'https?://\S+|www\.\S+'
    return bool(re.search(pattern, email))

email = "Visit https://google.com"

print(has_url(email))

SUSPICIOUS_KEYWORDS = {
    "urgent": 10,
    "verify": 10,
    "password": 20,
    "otp": 20,
    "bank": 10,
    "click": 10,
    "login": 15,
    "winner": 15,
    "prize": 15,
    "gift": 10,
    "account": 10,
    "security": 10,
    "limited": 10,
    "immediately": 10
}

def detect_keywords(email):
    email = email.lower()

    found = []

    score = 0

    for word, weight in SUSPICIOUS_KEYWORDS.items():

        if word in email:

            found.append(word)

            score += weight

    return found, score


TRUSTED_DOMAINS = [
    "google.com",
    "amazon.com",
    "paypal.com",
    "microsoft.com",
    "apple.com"
]

from urllib.parse import urlparse

def detect_fake_domain(email):

    urls = re.findall(r'https?://\S+', email)

    for url in urls:

        domain = urlparse(url).netloc.lower()

        if domain not in TRUSTED_DOMAINS:

            return domain

    return None

def calculate_threat_score(email):

    score = 0

    reasons = []

    if has_url(email):
        score += 25
        reasons.append("Suspicious URL Found")

    keywords, keyword_score = detect_keywords(email)

    score += keyword_score

    if keywords:
        reasons.append(
            "Keywords: " + ", ".join(keywords)
        )

    fake = detect_fake_domain(email)

    if fake:
        score += 25
        reasons.append(
            f"Unknown Domain: {fake}"
        )

    score = min(score, 100)

    return score, reasons

