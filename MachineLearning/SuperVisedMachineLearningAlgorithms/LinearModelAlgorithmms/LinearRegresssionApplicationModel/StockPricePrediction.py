import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1:  Reading The CSv data
from keras.losses import mse

df = pd.read_csv("infy_stock.csv",usecols=['Date', 'Close'], parse_dates=['Date'],index_col='Date')
print("The DataFrame is ")
print(df)

# 2: getting The Top 5 data From The Data Sets is
print(df.head(5))

# 3: getting The last 5 data From The data Sets is
print(df.tail(5))

print("The information Of The Give Data Set is ")
print(df.info)

plt.figure(figsize=(17,5))
stock_price = pd.concat([df.Close[:'2015-06-12']/2,df.Close['2015-06-15':]])
plt.plot(stock_price)
plt.title("Closing Price Adjusted",fontsize=20)
plt.show()

# Lets now Predict the Stock price based on various methods.
# We will predict the values on last 68 days in the series.
# We will use Mean squared error as a metrics to calculate the error in our prediction.
# We will compare the results of various methods at the end.

#helper function to plot the stock prediction
prev_values = stock_price.iloc[:180]
y_test = stock_price.iloc[180:]

def plot_pred(pred,title):
    plt.figure(figsize=(17,5))
    plt.plot(prev_values,label='Train')
    plt.plot(y_test,label='Actual')
    plt.plot(pred,label='Predicted')
    plt.ylabel("Stock prices")
    plt.title(title,fontsize=20)
    plt.legend()
    plt.show()

# 1. Average
# This is the simplest model. We will get as average of the previous values and predict it as the forecast.

#Average of previous values
y_av = pd.Series(np.repeat(prev_values.mean(),68),index=y_test.index)
print("The Average of The previous values & Predicted Values is ")
print(mse(y_av,y_test))

plot_pred(y_av,"Average")

# 2. Weighted Mean
# We shall give more weightage to the data which are close to the last day in training data,
# while calculating the mean. The last day in the training set will get a weightage of 1(=180/180)
# and the first day will get a weightage of 1/180.

weight = np.array(range(0,180))/180
weighted_train_data =np.multiply(prev_values,weight)

# weighted average is the sum of this weighted train data by the sum of the weight

weighted_average = sum(weighted_train_data)/sum(weight)
y_wa = pd.Series(np.repeat(weighted_average,68),index=y_test.index)
print("The Weigheted Average value is ")
print(mse(y_wa,y_test))
plot_pred(y_wa,"Weighted Average")

# For the other methods we will predict the value of stock price on a day based on the values of stock
# prices of 80 days prior to it. So in our series we will not consider the first eight days
# (since there previous eighty days is not in the series).
# We have to test the last 68 values. This would be based on the last 80 days stock prices of each day
# in the test data.
# Since we have neglected first 80 and last 68 is our test set, the train dataset will be between 80 and
# 180 (100 days).
y_train = stock_price[80:180]
y_test = stock_price[180:]
print("y train:",y_train.shape,"\ny test:",y_test.shape)

# There are 100 days in training and 68 days in testing set. We will construct the features,
# that is the last 80 days stock for each date in the y_train and y_test. This would be our target variable.

X_train = pd.DataFrame([list(stock_price[i:i+80]) for i in range(100)],
                       columns=range(80,0,-1),index=y_train.index)
X_test = pd.DataFrame([list(stock_price[i:i+80]) for i in range(100,168)],
                       columns=range(80,0,-1),index=y_test.index)

print("The Value Of The X Train is ")
print(X_train)
print("The Value Of The X Test is ")
print(X_test)

# X_train is now a collection of 100 dates as index and a collection of stock prices of previous 80 days
# as features.
# Similarlily, X_test is now a collection of 68 dates as index and a collection of stock prices of previous
# 80 days as features.
# NOTE: Here 76 working days from '2015-05-04', the stock had a price of 986.725 and 77 working days from
# '2015-05-05',
# the stock has the same value. You can see the similarity of values along the diagonal. This is
# because consecutitive data will be similar to the previous except it drops the last value, shifts
# and has a new value.We will use these values for stock price prediction in the other four methods.

# 3. Moving Average
# We have to predict the 68 values in data set and for each values we will get the average of
# previous 80 days.
# This will be a simple mean of each column in the y_test.

y_ma = X_test.mean(axis=1)
print(mse(y_ma,y_test))
plot_pred(y_ma,"Moving Average")

# 4. Weighted Moving Average
# We will obtain the stock price on the test date by calculating the weighted mean of past 80 days.
# The last of the 80 day will have a weightage of 1(=80/80) and the first will have a weightage of 1/80.

weight = np.array(range(1,81))/80
#weighted moving average
y_wma = X_test@weight/sum(weight)
print("The Weighted Moving Average is ")
print(mse(y_wma,y_test))

plot_pred(y_wma,"Weighted Moving Average")

# 4. Linear regression
# In this method, we will perform a linear regression on our dataset. The values will be predicted as
# a linear combination of the previous 80 days values.

from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(X_train,y_train)
y_lr = lr.predict(X_test)
print("The y_lr values is Using X-test is ")
print(y_lr)
y_lr = pd.Series(y_lr,index=y_test.index)
print("The y_lr Values is using y_lr ")
print(y_lr)
print(mse(y_test,y_lr))
plot_pred(y_lr,"Linear Regression")

# 6. Weighted Linear Regression
# We will provide weightage to our input data rather than the features.

weight = np.array(range(1,101))/100
wlr = LinearRegression()
wlr.fit(X_train,y_train,weight)
y_wlr = wlr.predict(X_test)
print("The Value Of The Y_wlr is using X_test ")
print(y_wlr)
y_wlr = pd.Series(y_wlr,index=y_test.index)
print("The Series  of The y_wlr is Using y_wlr is  ")
print(y_wlr)
print(mse(y_test,y_wlr))
plot_pred(y_wlr,"Weighted Linear Regression")
