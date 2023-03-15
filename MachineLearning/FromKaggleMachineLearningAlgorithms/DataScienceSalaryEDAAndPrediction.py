import numpy as np
import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.metrics import mean_squared_error
# 1 : First Step is To Read THe Data from the CSV FIle

df = pd.read_csv("ds_salaries.csv")
print("The Data Frame is ")
print(df)
print("The Top 10 Rows of The Data From The DataFrame is ")
print(df.head(10))

print("The info Of The Data is ")
print(df.info())

# Taking the Samples from The Data Frame is
print("The 5 Samples from The Above dataframe is  ")
print(df.sample(5))

# Getting The Shape Of The Data Frame is
print("The Shape Of The Data Frame is ")
print(df.shape)

# Describing The DataFrame
print(df.describe())

# Checking The Null values from The DataSets is
print("After Checking The Null values is ")
print(df.isnull().sum())

# Getting The Data type of The Data Sets is
print(df.dtypes)

# Now printing The Existing  Column Name Only from The Data Frame is
print("The Existing COlumn Names is ")
for col in df.columns:
    print(col)

# printing The Values With Column Name
print("After printing The values Count With Column Names is ")
for col in df.columns:
    print(col)
    print("++++++++++++++")
    print(df[col].value_counts())

# Now plotting The Work Experiences In Graph
print(sns.displot(df["work_year"]))

print(df.head())
print("The Difference BEtween The 2023 and Given date")
df["work_year"] = 2023 - df["work_year"]
print(df["work_year"])

from sklearn.preprocessing import OneHotEncoder
def category_to_column(df, column, prefix=''):
    df_copy = df.copy()
    oe_style = OneHotEncoder()
    oe_results = oe_style.fit_transform(df_copy[[column]])
    name_columns = prefix + oe_style.categories_[0]
    temp = pd.DataFrame(oe_results.toarray(), columns=name_columns, index=df_copy.index)
    df_copy = pd.concat([df_copy, temp], axis=1)
    return df_copy

from sklearn.preprocessing import OneHotEncoder
OHE = OneHotEncoder()
columns_category = ['experience_level']
for column in columns_category:
    df = category_to_column(df, column)
df = df.drop(columns=columns_category)
print("Aftre The USe of The drop()")
print(df.head())
df = df.drop(['job_title','salary','salary_currency','employee_residence','company_location'],axis = 1)
print("The Data Frame is ")
print(df)
print("The Head of The Data is ")
print(df.head(10))

from sklearn import linear_model
reg = linear_model.LinearRegression()

X=df.drop(['salary_in_usd'],axis=1)
y = df['salary_in_usd']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print("The Train Head Data Set is ")
print(X_train.head())

print("The Y Train Data Set is ")
print(y_train)
print("The x Train & yTrain Values is ")
# print(reg.fit(X_train, y_train))
print("The X Test Values is ")
print(X_test)
print("The Y Test Values is ")
print(y_test)


