import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import  sklearn
from sklearn.model_selection import train_test_split
# 1 : Loading The Data Set is
df = pd.read_csv("kc_house_data.csv")
print("The Data Set is ")
print(df)

# 2 : Getting The Space Data From The Given Data Set
spaces = df['sqft_living']
print("The SPaces of The Data From The Data set is ")
print(spaces)

# 3 : Getting The price details from The Given Data Set is
price = df['price']
print("Price from The Data Set is ")
print(price)

Maximum_SqaureFit_Area = max(spaces)
Maximum_Price_Area = max(price)
print("The MAximum Square Area is ",Maximum_SqaureFit_Area)
print("The Maximum Price is ",Maximum_Price_Area)

x = np.array(spaces).reshape(-1, 1)
y = np.array(price)
print("The Value Of The X is ")
print(x)
print("The Value Of The Y is ")
print(y)

#Splitting the data into Train and Test
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=1/3, random_state=0)

#Fitting simple linear regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xtrain, ytrain)

#Predicting the prices
pred = regressor.predict(xtest)
print("The Predicted Value is ")
print(pred)
#Visualizing the training Test Results
plt.scatter(xtrain, ytrain, color= 'red')
plt.plot(xtrain, regressor.predict(xtrain), color = 'blue')
plt.title ("Visuals for Training Dataset")
plt.xlabel("Space")
plt.ylabel("Price")
plt.show()

#Visualizing the Test Results
plt.scatter(xtest, ytest, color= 'red')
plt.plot(xtrain, regressor.predict(xtrain), color = 'blue')
plt.title("Visuals for Test DataSet")
plt.xlabel("Space")
plt.ylabel("Price")
plt.show()