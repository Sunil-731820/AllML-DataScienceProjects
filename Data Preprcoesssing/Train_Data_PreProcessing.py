import  pandas as pd
import numpy as np

df = pd.read_csv("train.csv")
print("The Data is : ")
print(df)

print("The Head of The Data is : ")
print(df.head())

# Step : 1 :
# 1. Data inspection and exploration:
# This step involves understanding the data by inspecting its structure and identifying missing values, outliers, and inconsistencies.
# Check the duplicate rows.

print("The Duplicated data Checking is ")
print(df.duplicated())

# Check the data information using df.info()

print("The data Information is : ")
print(df.describe())

# Check the categorical and numerical columns

cat_col = [col for col in df.columns if df[col].dtype=='object']
num_col = [col for col in df.columns if df[col].dtype!='object']

print("The Cat Column is : ",cat_col)
print("The Numerical column is : ",num_col)

# Check the total number of unique values in the Categorical columns
print("The Total Number of The unique Values in Categorical Column is : ")
print(df[cat_col].nunique())

# for Ticket lets print The 50 values first
print("The First 50 Tickets Are : ")
print(df['Ticket'].unique()[:50])

# Drop Name and Ticket columns.
df1 = df.drop(columns=["Name","Ticket"])
print("After Dropping The New Data Frame Is : ")
print(df1)


# Step 3 : Handling missing data:
'''
Missing data is a common issue in real-world datasets, and it can occur due to various reasons such as human errors, system failures, or data collection issues. Various techniques can be used to handle missing data, such as imputation, deletion, or substitution.
Let’s check the % missing values columns-wise for each row using df.isnull() it checks whether the values are null or not and gives returns boolean values. and .sum() will sum the total number of null values rows and we divide it by the total number of rows present in the dataset then we multiply to get values in % i.e per 100 values how much values are null.
'''
print("The number of Rows Having The Missing values is : ")
print(round((df1.isnull().sum()/df1.shape[0])*100,2))


df2 = df1.drop(columns='Cabin')
print("After Dropping The Cabin Column is : ")
print(df2)

print("After Dropping The Null ROws for This particular Column is : ")
print(df2.dropna(subset=['Embarked'], axis=0, inplace=True))
print(df2)


# Mean imputation
df3 = df2.fillna(df2.Age.mean())
print("The Data Frame 3 is : ")
print(df3)
# Let's check the null values again
print(df3.isnull().sum())

import matplotlib.pyplot as plt

plt.boxplot(df3['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
plt.show()

# calculate summary statistics
mean = df3['Age'].mean()
std = df3['Age'].std()

# Calculate the lower and upper bounds
lower_bound = mean - std * 2
upper_bound = mean + std * 2

print('Lower Bound :', lower_bound)
print('Upper Bound :', upper_bound)

# Drop the outliers
df4 = df3[(df3['Age'] >= lower_bound)
          & (df3['Age'] <= upper_bound)]
print("The Data Frame 4 Is : ")
print(df4)


X = df3[['Pclass','Sex','Age', 'SibSp','Parch','Fare','Embarked']]
Y = df3['Survived']
print("the Column Which is Independent is : ")
print(X)
print("The target variable is : ")
print(Y)

from sklearn.preprocessing import MinMaxScaler

# initialising the MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
print("The Value Of The Scalar is : ",scaler)
# Numerical columns
num_col_ = [col for col in X.columns if X[col].dtype != 'object']
print("the num Column is : ",num_col_)
x1 = X
# learning the statistical parameters for each of the data and transforming
x1[num_col_] = scaler.fit_transform(x1[num_col_])
print(x1.head())

