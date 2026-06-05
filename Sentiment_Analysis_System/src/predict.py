import pickle

model = pickle.load(
    open(r"C:\Users\User\Cantilever\Sentiment_Analysis_System\model\sentiment_model.pkl", "rb")
)

vectorizer = pickle.load(
    open(r"C:\Users\User\Cantilever\Sentiment_Analysis_System\model\vectorizer.pkl", "rb")
)

review = input("Enter movie review: ")

review_vector = vectorizer.transform([review])

prediction = model.predict(review_vector)

if prediction[0] == 1:
    print("Positive Review")
else:
    print("Negative Review")