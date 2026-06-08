# 🎓 Cantilever

Machine Learning Internship Projects using Python.

---

# 🎬 Sentiment Analysis System

## 📌 Project Description

The Sentiment Analysis System is a Machine Learning and Natural Language Processing (NLP) project that classifies movie reviews as **Positive** or **Negative**.

The model is trained on the **IMDb Movie Reviews Dataset (50,000 reviews)** and uses **TF-IDF Vectorization** along with **Logistic Regression** to perform sentiment classification.

This project demonstrates a complete Machine Learning workflow including:

* Data Preprocessing
* Text Cleaning
* Feature Extraction
* Model Training
* Model Evaluation
* Sentiment Prediction

---

## 🎯 Objective

To automatically determine the sentiment of a movie review by analyzing its text and classifying it as:

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

  * Positive Reviews
  * Negative Reviews

---

## ⚙️ Methodology

### 1. Data Preprocessing

* Convert text to lowercase
* Remove special characters and punctuation
* Remove stopwords using NLTK
* Clean and normalize review text

### 2. Feature Extraction

* Convert text into numerical vectors using TF-IDF Vectorization

### 3. Model Training

* Train a Logistic Regression classifier on the processed dataset

### 4. Model Evaluation

* Evaluate model performance using accuracy score

### 5. Prediction

* Predict whether a review is Positive or Negative

---

## 📈 Results

**Model Accuracy:** ~88.89%

### Example

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

Install required packages:

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

This project demonstrates the practical use of Machine Learning and Natural Language Processing techniques for sentiment classification. By combining TF-IDF Vectorization with Logistic Regression, the system achieves high accuracy and can be applied to various real-world text analysis tasks.
