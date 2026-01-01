
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
