import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report,accuracy_score,confusion_matrix
import seaborn as sns

# First Laod the using the CSv files

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(url, names=column_names)
print("The data is ")
print(data)

# Display the first few rows of the dataset
print(data.head())

# Separate the Features And the target variable
X = data.drop('Outcome',axis=1)
y = data['Outcome']

print("The Features Called As X is :")
print(X)

print("The target variable called y is :")
print(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an instance of Logistic Regression and fit the model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)

# Make predictions
y_pred = logreg.predict(X_test)

print("The predicted Value is ")
print(y_pred)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Visualize the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()


# Now I am trying to predict that Person has Disease or not

Pregnancies1 = 6,
Glucose1 = 148,
BloodPressure1 = 72,
SkinThickness1 = 35,
Insulin1 = 0,
BMI1 = 33.6,
DiabetesPedigreeFunction1 = 0.627,
Age = 50

# New patient data
new_patient = np.array([[
6,148,72,35,0,33.6,0.627,50
]])

# Predict the outcome for the new patient
new_patient_pred = logreg.predict(new_patient)
new_patient_proba = logreg.predict_proba(new_patient)
print("The value of the new_patient_pred is :",new_patient_pred)
print("The value of the new_patient_proba is :",new_patient_proba)

print("Prediction for the new patient:", "Diabetes" if new_patient_pred[0] == 1 else "No Diabetes")
print("Probability of each class (No Diabetes, Diabetes):", new_patient_proba[0])

