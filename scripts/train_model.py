import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


#  File Path

DATA_PATH = r"C:\Users\Sahana\Desktop\student-grades-project\data\processed\student_marks_processed.csv"


#  Load Dataset

df = pd.read_csv(DATA_PATH)

print("Processed Dataset Loaded Successfully ✅")
print("Shape:", df.shape)
print(df.head())


#  Features & Target

X = df.drop(columns=['Final_Marks'])
y = df['Final_Marks']


# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


#  Train Model

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Training Completed 🎯")


#  Predictions

y_pred = model.predict(X_test)


#  Model Evaluation

print("\nModel Performance:")
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("R2  :", r2_score(y_test, y_pred))


#  Save Model (Optional)

import joblib

MODEL_PATH = r"C:\Users\Sahana\Desktop\student-grades-project\models"
os.makedirs(MODEL_PATH, exist_ok=True)

joblib.dump(model, os.path.join(MODEL_PATH, "student_marks_model.pkl"))

print("\nModel saved successfully 💾")
