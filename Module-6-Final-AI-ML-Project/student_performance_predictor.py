# ============================================================
# Codomax AI & ML Internship
# Module 6 - Final AI & ML Project
# Student Performance Prediction using Machine Learning
# ============================================================

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# 1. Load Dataset
# ============================================================

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"

import zipfile
import requests
from io import BytesIO

response = requests.get(url)

with zipfile.ZipFile(BytesIO(response.content)) as z:
    with z.open("student-mat.csv") as file:
        df = pd.read_csv(file, sep=";")


print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)


# ============================================================
# 2. Explore Dataset
# ============================================================

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


# ============================================================
# 3. Check Missing Values
# ============================================================

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 4. Check and Remove Duplicate Rows
# ============================================================

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Dataset Shape After Removing Duplicates:")
print(df.shape)


# ============================================================
# 5. Select Features and Target
# ============================================================

features = [
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2"
]

target = "G3"

X = df[features]
y = df[target]

print("\nSelected Features:")
print(features)

print("\nTarget Variable:")
print(target)


# ============================================================
# 6. Data Visualization
# ============================================================

# Distribution of final grades
plt.figure(figsize=(8, 5))

plt.hist(df["G3"], bins=10)

plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")

plt.show()


# Study time vs final grade
plt.figure(figsize=(8, 5))

plt.scatter(df["studytime"], df["G3"])

plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")

plt.show()


# G2 vs final grade
plt.figure(figsize=(8, 5))

plt.scatter(df["G2"], df["G3"])

plt.title("Previous Grade (G2) vs Final Grade (G3)")
plt.xlabel("G2")
plt.ylabel("G3")

plt.show()


# ============================================================
# 7. Train/Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))


# ============================================================
# 8. Create and Train Machine Learning Model
# ============================================================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel training completed successfully!")


# ============================================================
# 9. Make Predictions
# ============================================================

y_pred = model.predict(X_test)

print("\nFirst 10 Predictions:")
print(y_pred[:10])


# ============================================================
# 10. Evaluate the Model
# ============================================================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("==============================")
print("Mean Absolute Error:", round(mae, 2))
print("Mean Squared Error:", round(mse, 2))
print("Root Mean Squared Error:", round(rmse, 2))
print("R² Score:", round(r2, 2))


# ============================================================
# 11. Actual vs Predicted Values
# ============================================================

comparison = pd.DataFrame({
    "Actual G3": y_test.values,
    "Predicted G3": np.round(y_pred, 2)
})

print("\nActual vs Predicted:")
print(comparison.head(15))


# ============================================================
# 12. Actual vs Predicted Visualization
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Final Grade")
plt.ylabel("Predicted Final Grade")
plt.title("Actual vs Predicted Final Grades")

plt.show()


# ============================================================
# 13. Feature Coefficients
# ============================================================

coefficients = pd.DataFrame({
    "Feature": features,
    "Coefficient": model.coef_
})

print("\nFeature Coefficients:")
print(coefficients)


plt.figure(figsize=(8, 5))

plt.bar(
    coefficients["Feature"],
    coefficients["Coefficient"]
)

plt.title("Feature Coefficients")
plt.xlabel("Feature")
plt.ylabel("Coefficient")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ============================================================
# 14. Predict a New Student
# ============================================================

new_student = pd.DataFrame({
    "studytime": [3],
    "failures": [0],
    "absences": [5],
    "G1": [14],
    "G2": [15]
})

prediction = model.predict(new_student)

predicted_score = prediction[0]


# ============================================================
# 15. Performance Interpretation
# ============================================================

if predicted_score >= 16:
    performance = "Excellent"

elif predicted_score >= 14:
    performance = "Very Good"

elif predicted_score >= 12:
    performance = "Good"

elif predicted_score >= 10:
    performance = "Average"

else:
    performance = "Needs Improvement"


print("\n==============================")
print("STUDENT PERFORMANCE PREDICTION")
print("==============================")

print("Predicted Final Grade:",
      round(predicted_score, 2))

print("Performance Level:",
      performance)


# ============================================================
# 16. Final Project Summary
# ============================================================

print("\n==============================")
print("FINAL PROJECT SUMMARY")
print("==============================")

print("Number of Students:", len(df))

print("Number of Features Used:",
      len(features))

print("Features Used:", features)

print("Target Variable:", target)

print("Training Samples:", len(X_train))

print("Testing Samples:", len(X_test))

print("R² Score:", round(r2, 2))

print("\nProject completed successfully!")
