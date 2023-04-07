import numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns # Advanced visualization
from sklearn.linear_model import LinearRegression
# Reading The dataSets Using pandas Lib
df = pd.read_csv("linear-regression-dataset.csv")
print("The data Set is ")
print(df)

# Showing The Top 5 data set is
print("The Top 5 Values is ")
print(df.head(5))

# Showing The last 5 data set is
print("The Last 5 values is ")
print(df.tail(5))

# Describing The Data Set is
print(df.describe())

# The Correlation of The given data Set is
print("The Correlation of The given Data set is ")
print(df.corr())

# Plotting and Visualizing The Given data Set
plt.scatter(df.experience,df.salary)
plt.ylabel("salary")
plt.xlabel("experience")
plt.show()

# Plotting The Data With the SubPlot

data_plot = df.loc[:,["experience","salary"]]
data_plot.plot()
plt.show()

# Heatmapping with Seaborn The Most Important Grah is This One Only used This One To get Best visualization In The OutPut
f,ax = plt.subplots(figsize=(20, 10))
sns.heatmap(df, annot=True, linewidths=0.5,linecolor="red", fmt= '.1f',ax=ax)
plt.show()

# 4 Model Fitting, Optimizing, and Predicting
# Now that our data has been processed and formmated properly,
# and that we understand the general data we're working with as well as the trends and associations,
# we can start to build our model. We can import different classifiers from sklearn.

linear_Reg = LinearRegression()
x = df.experience.values.reshape(-1,1)  # This Statement is Basically used for the getting The Whole column and Single Row
y = df.salary.values.reshape(-1,1) # This Statement is Basically used for the getting The Whole column and Single Row
print("After TheValue of The X is " , x)
print("After The Value Of  The Y is ",y)

# Its Time To Fit The Data
linear_Reg.fit(x,y)
print("The Linear regression fit Value is ")
print(linear_Reg.fit(x,y))

# Now Predicting The 20 Year Experinces Salary is
next_salary = linear_Reg.predict([[20]])
print("The Salary of The person having The Experiences of 20 Years ")
print(next_salary)

# Again Predicting The Salary of 30 Year Experinces Person
print("The Salary of 30 Year Experinces Person")
next_salary1 = linear_Reg.predict([[30]])
print("The Salary of The person is ")
print(next_salary1)

# predict the Salary of The person having The Experience of 0.9 Month (Its Mine Experiences Sunil Kumar Gupta Salary predictions)
sunil_Salary = linear_Reg.predict([[0.9]])
print("The Sunil Salary is ")
print(sunil_Salary)




