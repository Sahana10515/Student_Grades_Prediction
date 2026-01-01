import joblib
import pandas as pd


#  Load Model

model = joblib.load(r"C:\Users\Sahana\Desktop\student-grades-project\models\student_marks_model.pkl")
print("Model Loaded Successfully ✅")


#  User Input

print("\nEnter Student Details:")

data = {
    "Total_Study_Hours": [float(input("Total Study Hours in Module Area: "))],
    "Avg_Study_Percentage": [float(input("Average Study Percentage (0 to 1): "))],
    "Presence_Count": [float(input("Number of Presences: "))],
    "Absence_Count": [float(input("Number of Absences: "))],
    "Attendance_Percent": [float(input("Attendance Percentage: "))]
}


#  Convert to DataFrame

input_df = pd.DataFrame(data)


#  Prediction

predicted_marks = model.predict(input_df)

print("\n🎯 Predicted Final Marks:", round(predicted_marks[0], 2))
