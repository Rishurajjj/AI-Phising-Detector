
from feature_engineering import calculate_threat_score

def explain_email(email):

    score, reasons = calculate_threat_score(email)

    return score, reasons

