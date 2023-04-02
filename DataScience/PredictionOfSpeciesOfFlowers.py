import  pandas as pd
import  numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import  SVC

# 1: Load The Iris Data Sets using pandas Liabries
df  = pd.read_csv("IRIS.csv")
print("The Data sets is ")
print(df)

# 2 : split the Datasets into the Features & labels
x = df[['sepal_length','sepal_width','petal_length','petal_width']]
y = df['species']
print("The value Of The X is Called as The Features ")
print(x)
print("The Value Of The Y is called as The labels")
print(y)


# 3 : Splitting the Data into The Tranaining and Testing sets

X_train , X_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print("The X Trains parts is : " ,X_train)
print("The X Test parts is : " ,X_test)
print("The y Train parts is : ",y_train)
print("The Y Test parts is ",y_test)

# Creating The Model For This Predictions
model = SVC()
# For Training The Model Always Use The X_Train & Y_train parts
model.fit(X_train,y_train)

# For Accuracy The Model Use X_test & y_Test Parts
accuracy = model.score(X_test,y_test)
print("The Accuracy of The Model is ")
print(accuracy*100)


