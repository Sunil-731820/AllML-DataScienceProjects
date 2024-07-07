import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')

# Load the dataset
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/sms.tsv"
data = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# Display the first few rows of the dataset
print(data.head())

# Preprocess the dataset
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

data['message'] = data['message'].apply(preprocess_text)

# Feature extraction using TF-IDF vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['message'])
y = data['label'].apply(lambda x: 1 if x == 'spam' else 0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an instance of Logistic Regression and fit the model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)

# Make predictions
y_pred = logreg.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))



# Function to predict if a new email is spam or not
def predict_email(text):
    text = preprocess_text(text)
    text_vector = vectorizer.transform([text])
    prediction = logreg.predict(text_vector)
    return "Spam" if prediction[0] == 1 else "Not Spam"

# Example new email
new_email = "Congratulations! You've won a free lottery ticket. Click here to claim your prize."
print("Prediction for the new email:", predict_email(new_email))

# Again predicting the New EMail is
msg = "This is cow"
print("The New prediction is : ",predict_email(msg))

# Again Doing the Same Things

userInputMsg = "SIX chances to win CASH! From 100 to 20"
print("The new Prediction is :",predict_email(userInputMsg))

