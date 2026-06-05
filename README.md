# Cantilever
Machine Learning Internship Projects - Sentiment Analysis System and Credit Card Fraud Detection using Python.

# 🎬 Sentiment Analysis System

## 📌 Project Description

The Sentiment Analysis System is a Machine Learning and Natural Language Processing (NLP) project that classifies movie reviews as **Positive** or **Negative**. The system is trained on the IMDb Movie Reviews Dataset containing 50,000 reviews and uses TF-IDF vectorization along with Logistic Regression to predict sentiment accurately.

This project demonstrates the complete machine learning workflow including data preprocessing, feature extraction, model training, evaluation, and prediction.

---

## 🎯 Objective

The objective of this project is to automatically determine the sentiment expressed in a movie review by analyzing the review text and classifying it as positive or negative.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* Pickle

---

## 📂 Project Structure

```text
Sentiment_Analysis_System
│
├── data
│   └── IMDB Dataset.csv
│
├── model
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
│
├── src
│   ├── train_model.py
│   └── predict.py
│
└── requirements.txt
```

---

## 📊 Dataset Information

* Dataset: IMDb Movie Reviews Dataset
* Total Reviews: 50,000
* Classes:

  * Positive Reviews
  * Negative Reviews

---

## ⚙️ Methodology

### 1. Data Loading

The IMDb dataset is loaded using Pandas.

### 2. Data Preprocessing

Sentiment labels are converted into numerical values:

* Positive → 1
* Negative → 0

### 3. Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert textual reviews into numerical vectors.

### 4. Model Training

A Logistic Regression classifier is trained using the transformed review data.

### 5. Model Evaluation

The model is tested on unseen data and evaluated using accuracy score.

### 6. Model Saving

The trained model and vectorizer are saved using Pickle for future predictions.

---

## 🤖 Machine Learning Algorithm

### Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification tasks. It is efficient, fast, and performs well on text classification problems.

---

## 📈 Results

Model Accuracy:

```text
88.89%
```

The model successfully classifies movie reviews into positive and negative categories with high accuracy.

---

## 🚀 Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Train the Model

```bash
python src/train_model.py
```

### Predict Sentiment

```bash
python src/predict.py
```

Example:

```text
Enter movie review:
This movie was fantastic and amazing.
```

Output:

```text
Positive Review
```

---

## 💡 Applications

* Movie Review Classification
* Customer Feedback Analysis
* Product Review Analysis
* Social Media Monitoring
* Opinion Mining
* Business Analytics

---

## 🔮 Future Improvements

* Deep Learning Models (LSTM, GRU)
* BERT-based Sentiment Analysis
* Streamlit Web Application
* Real-time Prediction System
* Interactive Dashboard

---

## 🏆 Conclusion

This project successfully applies Natural Language Processing and Machine Learning techniques to classify movie reviews based on sentiment. By using TF-IDF vectorization and Logistic Regression, the system achieves high accuracy and demonstrates practical applications of sentiment analysis in real-world scenarios.

