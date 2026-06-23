# 🎓 Cantilever

Machine Learning Internship Projects using Python.

# 💳 Credit Card Fraud Detection System

## 📌 Project Description

The Credit Card Fraud Detection System is a Machine Learning project that identifies fraudulent credit card transactions as either legitimate or fraudulent.

The model is trained on the Credit Card Fraud Detection Dataset and uses a Random Forest Classifier to detect suspicious transactions with high accuracy.

This project demonstrates a complete Machine Learning workflow, including:

* Data Loading
* Data Preparation
* Feature Selection
* Model Training
* Model Evaluation
* Fraud Prediction

## 🎯 Objective

To automatically detect fraudulent credit card transactions and help improve financial security by identifying suspicious activities.

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier
* Pickle

## 📂 Project Structure

```text
Credit_Card_Fraud_Detection/
│
├── data/
│   └── dataset_note.txt
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

## 📊 Dataset Information

Dataset: Credit Card Fraud Detection Dataset

Total Transactions: 284,807

Total Features: 30

Target Column: Class

### Class Labels

* 0 → Normal Transaction
* 1 → Fraudulent Transaction

The dataset is highly imbalanced, with fraudulent transactions representing a very small percentage of all transactions.

## ⚙️ Methodology

### 1. Data Loading

The dataset is loaded using Pandas.

### 2. Data Preparation

* Separate features and target variable
* Define input and output data

### 3. Train-Test Split

The dataset is divided into training and testing sets.

### 4. Model Training

A Random Forest Classifier is trained using the prepared dataset.

### 5. Model Evaluation

The model is evaluated using accuracy score.

### 6. Model Saving

The trained model is saved as:

```text
model/fraud_model.pkl
```

### 7. Fraud Prediction

The saved model is loaded to predict whether a transaction is normal or fraudulent.

## 🤖 Machine Learning Algorithm

### Random Forest Classifier

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting. It is widely used for classification tasks and performs well on structured datasets such as fraud detection problems.

## 📈 Results

### Model Accuracy

Accuracy: ~99.95%

The model successfully identifies normal and fraudulent transactions with high accuracy.

### Example Output

Output:

```text
Normal Transaction
```

## 🚀 Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

### Train the Model

```bash
python src/train_model.py
```

### Predict Transaction

```bash
python src/predict.py
```

## 📥 Dataset

The dataset is not included in this repository because it exceeds GitHub's file size limit.

The `data/` folder contains a note file:

dataset_note.txt

It explains how to use the dataset.


## 💡 Applications

* Banking Security Systems
* Online Payment Fraud Detection
* Financial Risk Management
* Transaction Monitoring
* Digital Payment Platforms

## 🔮 Future Improvements

* XGBoost Classifier
* Deep Learning Models
* Real-Time Fraud Detection
* Streamlit Web Application
* Interactive Dashboard
* Hyperparameter Tuning

## 🏆 Conclusion

This project demonstrates the practical application of Machine Learning for detecting fraudulent credit card transactions. By using a Random Forest Classifier, the system achieves high accuracy and can help financial institutions improve transaction security and reduce fraud-related losses.

## 👩‍💻 Author

Jashanpreet Kaur

B.Tech, Computer Science and Engineering

National Institute of Technology Hamirpur

GitHub Profile: https://github.com/jashan0987
