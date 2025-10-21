import joblib
from handle_messages import clean_message

vectorizer = None
model = None
LABEL_MAP = {
    0: "negative",
    1: "neutral",
    2: "positive"
}

def load_model():
    global vectorizer, model
    if vectorizer is None or model is None:
        vectorizer = joblib.load("models/vectorizer.joblib")
        model = joblib.load("models/logistic_regression.joblib")
        print("Model loaded successfully!")


def predict_sentiments(messages: list[str]):
    clean_msgs = [clean_message(m) for m in messages]
    X = vectorizer.transform(clean_msgs)

    pre = model.predict(X)
    probs = model.predict_proba(X)

    results = []
    for msg, pred, prob in zip(messages, pre, probs):
        results.append({
            "message": msg,
            "label": LABEL_MAP.get(int(pred), "unknown"),
            "confidence": float(max(prob) * 100)
        })
    return results
