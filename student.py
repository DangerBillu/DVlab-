
import pandas as pd
import numpy as np

df = pd.read_csv("student.csv")
print("printing first 5 rows")
print(df.head())

numericols = ["StudentID", "MathScore", "ReadingScore", "WritingScore", "StudyHours", "Attendance"]
df[numericols] = df[numericols].replace(-1, np.nan)
for column in numericols:
    mean = df[column].mean()
    df[column] = df[column].fillna(mean)
print("replaced")
print(df[numericols].describe())

for column in numericols:
    median = df[column].median()
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3-q1

    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr

    df[column] = np.where((df[column]<lower) | (df[column]>upper), median, df[column])
    
print("replaced")
print(df[numericols].describe())

print("printing first 5 rows")
print(df.head())
