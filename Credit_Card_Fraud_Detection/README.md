# 💳 Credit Card Fraud Detection System

## 📌 Project Description

The Credit Card Fraud Detection System is a Machine Learning project designed to identify fraudulent credit card transactions. The model is trained on a real-world credit card transaction dataset and classifies transactions as either legitimate or fraudulent.

This project demonstrates a complete Machine Learning workflow, including data loading, preprocessing, model training, evaluation, prediction, and model deployment preparation.

---

## 🎯 Objective

The objective of this project is to automatically detect fraudulent credit card transactions and help improve financial security by identifying suspicious activities.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier
* Pickle

---

## 📂 Project Structure

```text
Credit_Card_Fraud_Detection/
│
├── data/
│   └── creditcard.csv
│
├── model/
│   └── fraud_model.pkl
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

* Dataset: Credit Card Fraud Detection Dataset
* Total Transactions: 284,807
* Total Features: 30
* Target Column: Class

### Class Labels

* 0 → Normal Transaction
* 1 → Fraudulent Transaction

The dataset is highly imbalanced, with fraudulent transactions representing a very small percentage of the total transactions.

---

## ⚙️ Methodology

### 1. Data Loading

The dataset is loaded using Pandas.

### 2. Data Preparation

* Separate features and target variable.
* Define input and output data.

### 3. Train-Test Split

The dataset is split into training and testing sets.

### 4. Model Training

A Random Forest Classifier is trained using the training dataset.

### 5. Model Evaluation

The trained model is evaluated using accuracy score.

### 6. Model Saving

The trained model is saved as:

```text
model/fraud_model.pkl
```

### 7. Prediction

The saved model is loaded and used to predict whether a transaction is normal or fraudulent.

---

## 📈 Results

### Model Accuracy

```text
Accuracy: 99.95%
```

### Example Output

```text
Normal Transaction
```

The model successfully identifies normal and fraudulent transactions with high accuracy.

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

### Predict Transaction

```bash
python src/predict.py
```

---

## 📥 Dataset

The dataset is not included in this repository because it exceeds GitHub's file size limit.

Download the Credit Card Fraud Detection Dataset and place:

```text
creditcard.csv
```

inside the `data/` folder before running the project.

---

## 💡 Applications

* Banking Security Systems
* Online Payment Fraud Detection
* Financial Risk Management
* Transaction Monitoring
* Digital Payment Platforms

---

## 🔮 Future Improvements

* XGBoost Classifier
* Deep Learning Models
* Real-Time Fraud Detection
* Streamlit Web Application
* Interactive Dashboard
* Hyperparameter Tuning

---

## 🏆 Conclusion

This project demonstrates the practical application of Machine Learning for detecting fraudulent credit card transactions. By using a Random Forest Classifier, the system achieves high accuracy and can help financial institutions improve transaction security and reduce fraud-related losses.

---

## 👩‍💻 Author

**Jashanpreet Kaur**

B.Tech Computer Science and Engineering

National Institute of Technology Hamirpur

GitHub: https://github.com/jashan0987
