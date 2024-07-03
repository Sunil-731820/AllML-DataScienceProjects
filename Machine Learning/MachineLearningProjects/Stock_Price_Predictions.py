# import all the necessary libraries

from datetime import datetime
import numpy as np
import pandas as pd
import  datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# Loading the CSV data from the CSV file
df = pd.read_csv("stock_data.csv")
print("The Head of the Data is ")
print(df.head())

#Preprocess the Data
# For simplicity, let's predict the Close price based on the Open, High, Low, and Volume.

# Convert Date to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Define features and target variable
X = df[['Open', 'High', 'Low', 'Volume']]  # This is The Input for that variable i.e feature label
y = df['Close']  # This is The target Variable  i.e called as target label

print("The Value of the X is :")
print(X)
print("The value of the Y is :")
print(y)

# Split the Data
# Split the data into training and testing sets.

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Train the Model
# Use the Linear Regression model from scikit-learn

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Evaluate the Model
# Evaluate the model using the test data.

 # Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R-squared: {r2}")

# Interpret Results
# Analyze the coefficients to understand the relationship between features and the target variable.

print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")

# Visualize the Results
# Visualize the actual vs. predicted prices.
# Plot actual vs. predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs. Predicted Prices')
plt.show()

# Now I am going to Predict the Data for given Below Observations

# 1 : Date : 2023-01-01
# 2 : Open : 135.67
# 3 : High : 137.50
# 4 : Low : 134.89
# 5 : Close : 136.50
# 6 : Volume : 3500000

# Commented By Sunil below code Because of Date is not able to convert into the String into Numbers format
# usergivenDate = 2023-01-01

'''


usergivenDate = '2023-01-01'
# Convert the string to a datetime object
timestamp_int = int(usergivenDate.timestamp())
# Convert the datetime object to a timestamp
print("The timestamp_int is :",timestamp_int)
'''
openValue = 135.67
HighValue = 137.50
Low = 134.89
Volume = 3500000

predcitedStockValue = model.predict([[openValue,HighValue,Low,Volume]])
print("The predicted Stock value is ")
print(predcitedStockValue)
