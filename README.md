# 🎓 Cantilever  
Machine Learning Internship Projects  
**Sentiment Analysis System & Credit Card Fraud Detection using Python**

---

# 🎬 Sentiment Analysis System

## 📌 Project Description

The **Sentiment Analysis System** is a Machine Learning and Natural Language Processing (NLP) project that classifies movie reviews as **Positive** or **Negative**.

The model is trained on the **IMDb Movie Reviews Dataset (50,000 reviews)** and uses **TF-IDF Vectorization** along with **Logistic Regression** to perform sentiment classification.

This project demonstrates a complete ML pipeline including:
- Data preprocessing  
- Text cleaning  
- Feature extraction  
- Model training  
- Evaluation  
- Prediction  

---

## 🎯 Objective

To automatically determine the sentiment of a movie review by analyzing text and classifying it as:

- 👍 Positive
- 👎 Negative

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK (for text preprocessing)  
- TF-IDF Vectorization  
- Logistic Regression  
- Pickle (Model saving)  

---

## 📂 Project Structure

```text
Sentiment_Analysis_System/
│
├── data/
│   └── IMDB Dataset.csv
│
├── preprocessing/
│   └── clean_text.py
│
├── model/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
│
├── src/
│   ├── train_model.py
│   └── predict.py
│
├── requirements.txt
└── README.md