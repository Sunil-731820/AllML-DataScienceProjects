import  matplotlib.pyplot as plt
import  pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  mean_absolute_error,mean_squared_error,r2_score

# Loading The Data using CsV file Method

df = pd.read_csv("housing_prediction.csv")
# Display first few rows
print(df.head())

# Extracting the Features from Te Csv file okay
# Preprocess the Data
# In this case, our data is clean, so we can proceed to define the features and target variable.

# Define features and target variable
X = df[['Size', 'Bedrooms', 'Bathrooms']]
y = df['Price']

# Split the Data
# Split the data into training and testing sets

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

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
# Analyze the coefficients to understand the relationship between features and the target variable

print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")


# Plot actual vs. predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs. Predicted Prices')
plt.show()

# let Suppose an Employee has the
# Size of the House = 3000
# Number of the bedrooms = 3
# Number of The bathrooms = 3

sizeOfEmployeeRoom = 2450
numberOfBedRooms = 4
numberOfBathrooms = 3

predictedPrice = model.predict([[sizeOfEmployeeRoom,numberOfBedRooms,numberOfBathrooms]])
print("The Predicted Price for that employee room size ")
print(predictedPrice)
print(f"Predicted Price for {sizeOfEmployeeRoom,numberOfBedRooms,numberOfBathrooms} is: {predictedPrice[0]}")




