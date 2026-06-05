import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv(r"C:\Users\User\Cantilever\Sentiment_Analysis_System\data\IMDB Dataset.csv")

# Convert labels
df["sentiment"] = df["sentiment"].map({
    "positive": 1,
    "negative": 0
})

# Features and labels
X = df["review"]
y = df["sentiment"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Save model
pickle.dump(
    model,
    open(r"C:\Users\User\Cantilever\Sentiment_Analysis_System\model\sentiment_model.pkl", "wb")
)

pickle.dump(
    vectorizer,
    open(r"C:\Users\User\Cantilever\Sentiment_Analysis_System\model\vectorizer.pkl", "wb")
)