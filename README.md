# 🎓 Cantilever

Machine Learning Internship Projects using Python.

## 🎬 Sentiment Analysis System

### 📌 Project Description

The Sentiment Analysis System is a Machine Learning and Natural Language Processing (NLP) project that classifies movie reviews as **Positive** or **Negative**.

The model is trained on the **IMDb Movie Reviews Dataset (50,000 reviews)** and uses **TF-IDF Vectorization** along with **Logistic Regression** for sentiment classification.

This project demonstrates a complete Machine Learning pipeline including:

* Data preprocessing
* Text cleaning
* Feature extraction
* Model training
* Model evaluation
* Prediction

---

## 🎯 Objective

To automatically determine the sentiment of a movie review by analyzing text and classifying it as:

* 👍 Positive
* 👎 Negative

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* TF-IDF Vectorization
* Logistic Regression
* Pickle

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
```

---

## 📊 Dataset Information

* Dataset: IMDb Movie Reviews Dataset
* Total Reviews: 50,000
* Classes:
<<<<<<< HEAD

  * Positive Reviews
  * Negative Reviews
=======
* Positive Reviews
* Negative Reviews
>>>>>>> d66c13c (Update README)

---

## ⚙️ Methodology

### 1. Data Preprocessing

* Convert text to lowercase
* Remove punctuation
* Remove stopwords using NLTK
* Clean review text

### 2. Feature Extraction

* TF-IDF Vectorization

### 3. Model Training

* Logistic Regression Classifier

### 4. Model Evaluation

* Accuracy Score

### 5. Prediction

* Predict whether a review is Positive or Negative

---

## 📈 Results

**Model Accuracy: ~88.89%**

Example:

**Input**

```text
This movie was fantastic and amazing.
```

**Output**

```text
Positive Review
```

---

## 🚀 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Train the model:

```bash
python src/train_model.py
```

Predict sentiment:

```bash
python src/predict.py
```

---

## 💡 Applications

* Movie Review Analysis
* Product Review Analysis
* Customer Feedback Analysis
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

This project demonstrates the use of NLP and Machine Learning techniques to classify movie reviews based on sentiment. Using TF-IDF Vectorization and Logistic Regression, the system achieves high accuracy and has practical real-world applications.
