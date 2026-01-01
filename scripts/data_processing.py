import pandas as pd
import os


# File Paths

DATA_PATH = r"C:\Users\Sahana\Desktop\student-grades-project\data\original\original.csv"   # change name if needed
OUTPUT_PATH = r"C:\Users\Sahana\Desktop\student-grades-project\data\processed"

os.makedirs(OUTPUT_PATH, exist_ok=True)


# Load Dataset (FIXED)

df = pd.read_csv(DATA_PATH, sep=",", engine="python")

print("Dataset Loaded Successfully ✅")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)


#  Clean Column Names

df.columns = df.columns.str.strip()


#  Select Useful Columns

selected_columns = [
    'Total Hours in Module Area',
    '% of Average Hours in Module Area',
    '# of presence',
    '# of Absence',
    'Percent Attended',
    'label (fail=1, pass=0)'
]

df = df[selected_columns]


#  Rename Columns (Simple Names)

df.rename(columns={
    'Total Hours in Module Area': 'Total_Study_Hours',
    '% of Average Hours in Module Area': 'Avg_Study_Percentage',
    '# of presence': 'Presence_Count',
    '# of Absence': 'Absence_Count',
    'Percent Attended': 'Attendance_Percent',
    'label (fail=1, pass=0)': 'Fail_Label'
}, inplace=True)


#  Convert Classification → Regression

# Fail=1, Pass=0 → Convert to Marks
df['Final_Marks'] = df['Attendance_Percent'] * (1 - df['Fail_Label'])

df.drop(columns=['Fail_Label'], inplace=True)


# Handle Missing Values

df = df.dropna()


#  Save Processed Data

processed_file = os.path.join(OUTPUT_PATH, "student_marks_processed.csv")
df.to_csv(processed_file, index=False)

print("\nData Processing Completed 🎉")
print("Saved at:", processed_file)
print(df.head())
