
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

messages = [
    "Your account password must be verified immediately",
    "Click here to verify your bank account",
    "Urgent: your account will be blocked",
    "Confirm your credentials to restore account access",
    "Your meeting is scheduled for tomorrow",
    "Please review the team meeting agenda",
    "The project discussion starts at 10 AM",
    "Thank you for sharing the meeting notes",
    "Your payment failed, update your card details",
    "Claim your free prize by clicking this link",
    "Your order has been shipped successfully",
    "The class assignment is due on Friday",
]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(messages)

model = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = model.fit_predict(X)

results = pd.DataFrame({
    "Message": messages,
    "Cluster": clusters
})

print("=== CyberShield Message Clustering ===")
for cluster_id in sorted(results["Cluster"].unique()):
    print(f"\nCluster {cluster_id}:")
    for message in results.loc[
        results["Cluster"] == cluster_id, "Message"
    ]:
        print("-", message)

print("\nNote: Cluster numbers are arbitrary and do not mean safe or malicious.")
