
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Small demonstration dataset.
# Add more diverse, verified examples before real-world use.
data = [
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

df = pd.DataFrame(data, columns=["message", "label"])

X_train, X_test, y_train, y_test = train_test_split(
    df["message"],
    df["label"],
    test_size=0.30,
    random_state=42,
    stratify=df["label"]
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("=== CyberShield ML Classification ===")
print(f"Training examples: {len(X_train)}")
print(f"Testing examples: {len(X_test)}")
print(f"Test accuracy: {accuracy:.2%}")
print("\nClassification report:")
print(classification_report(y_test, predictions, zero_division=0))

print("\nEnter a message to classify.")
message = input("Message: ").strip()

if message:
    prediction = model.predict([message])[0]
    print("ML prediction:", prediction)
    print("Note: This is a small demonstration model, not a reliable security verdict.")
else:
    print("No message entered.")
