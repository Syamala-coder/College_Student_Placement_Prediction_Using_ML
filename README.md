# 🎓 College Student Placement Prediction 

### 📌 Project Overview
This project focuses on predicting whether a student will be placed or not placed based on academic, technical, and skill-based attributes using Machine Learning classification models. The goal is to assist educational institutions and students in understanding the key factors influencing placement outcomes.

### 🎯 Problem Statement
To build a machine learning model that accurately predicts student placement status using historical academic performance, skill metrics, and experiential factors.

### 📂 Dataset Description
The dataset consists of 10,000 student records with a mix of numerical and categorical features, capturing academic performance, skills, and experience.

#### 🔹 Key Features
IQ

Previous Semester Result

CGPA

Academic Performance

Internship Experience

Extra Curricular Score

Communication Skills

Projects Completed

### 🎯 Target Variable
Placement (Yes / No)

## 🧪 Exploratory Data Analysis
Verified absence of null values and duplicates

Dropped irrelevant identifiers (College ID)

Analyzed feature distributions and outliers using boxplots

Observed class imbalance in placement outcomes

## ⚙️ Machine Learning Models Used
K-Nearest Neighbors (KNN)

Decision Tree Classifier

Naive Bayes Classifier

#### Each model was evaluated using:
Accuracy

Precision

Recall

F1-Score

Confusion Matrix

## 📊 Model Performance Summary
Decision Tree achieved the best balance between accuracy and recall for placed students.

KNN showed strong overall accuracy with consistent predictions.

Naive Bayes performed reasonably but was sensitive to preprocessing.

Hyperparameter tuning and pipelines were applied to ensure:

No data leakage

Consistent preprocessing

Reliable evaluation

## 🚀 Deployment
The final model was deployed using Streamlit, providing an interactive web interface where users can:

Enter student details

Predict placement outcome in real time

Visualize results in a clean, user-friendly UI

## 🛠️ Technologies Used
Python

Pandas, NumPy

Scikit-learn

Matplotlib, Seaborn

Streamlit

Pickle

# ✅ Conclusion
This project demonstrates an end-to-end machine learning workflow—from data preprocessing and model building to evaluation and deployment—highlighting the practical application of ML in educational analytics.
