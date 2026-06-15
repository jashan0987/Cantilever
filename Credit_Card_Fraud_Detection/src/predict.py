import os
import pickle
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "model", "fraud_model.pkl")
data_path = os.path.join(BASE_DIR, "data", "creditcard.csv")

with open(model_path, "rb") as file:
    model = pickle.load(file)

df = pd.read_csv(data_path)

sample = df.drop("Class", axis=1).iloc[[0]]

prediction = model.predict(sample)

if prediction[0] == 0:
    print("Normal Transaction")
else:
    print("Fraudulent Transaction")