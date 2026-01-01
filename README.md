# 🎓 Student Marks Prediction using Machine Learning

## 📌 Project Overview
This project predicts **student final marks** based on their **study engagement and attendance behavior** using **Machine Learning (Linear Regression)**.

The system analyzes factors such as:
- Total study hours
- Attendance percentage
- Presence and absence count
- Study activity metrics

The goal is to understand how these factors influence academic performance and to predict expected marks for new students.

---

## 🎯 Objectives
- Perform data preprocessing and cleaning
- Conduct Exploratory Data Analysis (EDA)
- Build a regression model to predict student marks
- Evaluate model performance
- Predict marks for new student inputs

---

## 🧠 Machine Learning Technique
- **Model Used:** Linear Regression  
- **Type:** Supervised Learning (Regression)

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Libraries:**
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Scikit-learn
  - Joblib

---

## 📁 Project Folder Structure
Student_Marks_Prediction/
│
├── data/
│ ├── original/ # Raw dataset
│ ├── processed/ # Cleaned dataset
│
├── notebooks/
│ └── student_marks_prediction.ipynb
│
├── scripts/
│ ├── data_processing.py
│ ├── train_model.py
│ └── predict_marks.py
│
├── models/
│ └── student_marks_model.pkl
│
├── README.md

---

## 📊 Dataset Description
- Source: Kaggle (Student Grades Prediction Dataset)
- Total Records: 78
- Target Variable: `Final_Marks`
- Features Used:
  - Total_Study_Hours
  - Avg_Study_Percentage
  - Presence_Count
  - Absence_Count
  - Attendance_Percent

---

## 🔍 Exploratory Data Analysis (EDA)
EDA was performed to:
- Understand data distribution
- Analyze correlations
- Identify relationships between attendance, study behavior, and marks

Visualizations include:
- Histograms
- Scatter plots
- Correlation heatmap

---

## 🧪 Model Training & Evaluation

### Evaluation Metrics:
- **MAE (Mean Absolute Error):** ~15
- **MSE (Mean Squared Error):** ~620
- **R² Score:** ~0.43

> The moderate R² score is expected as the dataset was originally designed for classification (pass/fail) and later adapted for regression.

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```
### 2️⃣ Run Data Processing
```bash
python scripts/data_processing.py
```
### 3️⃣ Train the Model
```bash
python scripts/train_model.py
```
### 4️⃣ Predict Marks
```bash
python scripts/predict_marks.py
```

### 🎯 Sample Prediction

Input:
- Study Hours: 6
- Attendance: 80%

Output:
🎯 Predicted Final Marks: 45.54

### 🎓 Use Cases

- Academic performance analysis

- Student engagement monitoring

- Early identification of low-performing students

- Educational data analytics projects

### 📌 Conclusion

This project demonstrates a complete end-to-end machine learning pipeline, from data preprocessing to prediction. It highlights how student engagement metrics significantly influence academic outcomes.

### 👨‍💻 Author

Sahana R
B.Tech – Artificial Intelligence & Data Science
St. Joseph College of Engineering

### ⭐ Acknowledgements

- Kaggle for the dataset

- Scikit-learn documentation

- Open-source Python community
