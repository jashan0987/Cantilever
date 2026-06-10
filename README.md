# 🎓 Cantilever

Machine Learning Internship Projects using Python.

---

# 🎬 Sentiment Analysis System

## 📌 Project Description

The Sentiment Analysis System is a Machine Learning and Natural Language Processing (NLP) project that classifies movie reviews as **Positive** or **Negative**.

The model is trained on the **IMDb Movie Reviews Dataset (50,000 reviews)** and uses **TF-IDF (Term Frequency–Inverse Document Frequency) Vectorization** along with **Logistic Regression** to perform sentiment classification.

This project demonstrates a complete Machine Learning workflow, including:

* Data Preprocessing
* Text Cleaning
* Feature Extraction
* Model Training
* Model Evaluation
* Sentiment Prediction

---

## 🎯 Objective

To automatically determine the sentiment expressed in a movie review by analyzing the review text and classifying it as:

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

* **Dataset:** IMDb Movie Reviews Dataset
* **Total Reviews:** 50,000
* **Classes:**

  * Positive Reviews
  * Negative Reviews

---

## ⚙️ Methodology

### 1. Data Preprocessing

The review text is cleaned before training the model:

* Convert text to lowercase
* Remove punctuation and special characters
* Remove stopwords using NLTK
* Normalize and clean review text

### 2. Feature Extraction

The cleaned text is converted into numerical vectors using **TF-IDF Vectorization**.

### 3. Model Training

A **Logistic Regression** classifier is trained using the processed dataset.

### 4. Model Evaluation

The model is evaluated using accuracy score on unseen test data.

### 5. Sentiment Prediction

The trained model predicts whether a movie review is positive or negative.

---

## 🤖 Machine Learning Algorithm

### Logistic Regression

Logistic Regression is a supervised machine learning algorithm commonly used for binary classification tasks. It is efficient, fast, and performs well on text classification problems such as sentiment analysis.

---

## 📈 Results

### Model Accuracy

**Accuracy: ~88.89%**

The model successfully classifies movie reviews into Positive and Negative sentiments with high accuracy using TF-IDF Vectorization and Logistic Regression.

### Example 1

**Input**

```text
This movie was fantastic and amazing.
```

**Output**

```text
Positive Review
```

### Example 2

**Input**

```text
This movie was boring and a waste of time.
```

**Output**

```text
Negative Review
```

---

## 🚀 Installation

Install the required dependencies:

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

This project demonstrates the practical application of Machine Learning and Natural Language Processing techniques for sentiment classification. By combining TF-IDF Vectorization with Logistic Regression, the system achieves high accuracy and can be applied to various real-world text analysis tasks.

---

## 👩‍💻 Author

**Jashanpreet Kaur**

B.Tech, Computer Science and Engineering
National Institute of Technology Hamirpur

GitHub Profile: https://github.com/jashan0987
