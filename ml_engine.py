
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

# Small demonstration dataset, not production training data.
DATA = [
    ("Your meeting is scheduled for tomorrow at 10 AM", "Normal"),
    ("Please find the notes from our team meeting", "Normal"),
    ("The class assignment is due on Friday", "Normal"),
    ("Your order has been shipped successfully", "Normal"),
    ("Can we reschedule our appointment to Monday", "Normal"),
    ("Thank you for sharing the project report", "Normal"),
    ("The lecture starts at 9 AM in room 204", "Normal"),
    ("Please review the attached meeting agenda", "Normal"),
    ("Your library book is due next week", "Normal"),
    ("The project presentation is scheduled for Wednesday", "Normal"),
    ("Urgent! Verify your account password immediately", "Suspicious"),
    ("Your account will be blocked click this link now", "Suspicious"),
    ("Confirm your bank details to avoid account suspension", "Suspicious"),
    ("Congratulations you won a prize claim it now", "Suspicious"),
    ("Enter your password to restore access immediately", "Suspicious"),
    ("Unusual login detected verify your account here", "Suspicious"),
    ("Your payment failed update your card details now", "Suspicious"),
    ("Act now or your account will be permanently closed", "Suspicious"),
    ("Click this link to claim your free reward", "Suspicious"),
    ("Confirm your credentials to prevent account closure", "Suspicious"),
]

messages = [item[0] for item in DATA]
labels = [item[1] for item in DATA]

# Train the classifier.
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.30,
    random_state=42,
    stratify=labels
)

classifier = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("model", LogisticRegression(max_iter=1000))
])

classifier.fit(X_train, y_train)

test_predictions = classifier.predict(X_test)
MODEL_ACCURACY = accuracy_score(y_test, test_predictions)

# Fit clustering separately, without using message labels.
cluster_vectorizer = TfidfVectorizer(stop_words="english")
cluster_features = cluster_vectorizer.fit_transform(messages)

cluster_model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)
cluster_model.fit(cluster_features)


def analyze_ml(message):
    """Return demonstration ML prediction and nearest cluster assignment."""
    prediction = classifier.predict([message])[0]

    message_features = cluster_vectorizer.transform([message])
    cluster_id = int(cluster_model.predict(message_features)[0])

    return {
        "prediction": prediction,
        "cluster": cluster_id,
        "test_accuracy": round(MODEL_ACCURACY * 100, 2),
        "model_note": (
            "Demonstration model trained on only 20 sample messages. "
            "Predictions may be wrong and must not be treated as proof."
        )
    }
