# 🎓 Cantilever

Machine Learning Internship Projects using Python

This repository contains two complete Machine Learning projects developed as part of an internship:

1. 🎬 Sentiment Analysis System (NLP Project)
2. 💳 Credit Card Fraud Detection System (Classification Project)

---

# 🎬 Sentiment Analysis System

## 📌 Project Description

The Sentiment Analysis System is a Natural Language Processing (NLP) project that classifies movie reviews as **Positive** or **Negative**.

The model is trained on the IMDb Movie Reviews Dataset (50,000 reviews) using **TF-IDF Vectorization** and **Logistic Regression**.

This project demonstrates a complete Machine Learning pipeline including:

- Data Preprocessing
- Text Cleaning
- Feature Extraction
- Model Training
- Model Evaluation
- Sentiment Prediction

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
- NLTK  
- TF-IDF Vectorizer  
- Logistic Regression  
- Pickle  

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
📊 Dataset Information
Dataset: IMDb Movie Reviews Dataset
Total Reviews: 50,000
Classes:
Positive Reviews
Negative Reviews
⚙️ Methodology
1. Data Preprocessing
Convert text to lowercase
Remove punctuation & special characters
Remove stopwords using NLTK
2. Feature Extraction
TF-IDF Vectorization used to convert text into numerical form
3. Model Training
Logistic Regression classifier trained on processed data
4. Model Evaluation
Accuracy score used for evaluation
5. Prediction
Model predicts sentiment of unseen movie reviews
📈 Results
Model Accuracy: ~88.89%
Example

Input:
This movie was fantastic and amazing.

Output:
Positive Review

🚀 Installation
pip install -r requirements.txt
▶️ Run Project
python src/train_model.py
python src/predict.py
💡 Applications
Movie Review Analysis
Product Review Analysis
Social Media Monitoring
Opinion Mining
Business Analytics
🔮 Future Improvements
Deep Learning (LSTM, GRU)
BERT-based models
Streamlit Web App
Real-time sentiment analysis
👩‍💻 Author

Jashanpreet Kaur
B.Tech CSE, NIT Hamirpur
GitHub: https://github.com/jashan0987