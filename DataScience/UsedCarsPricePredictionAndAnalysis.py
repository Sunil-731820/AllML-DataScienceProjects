import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("UsedCarsDataSets.csv")
print("The data Set is ")
print(data)

print("The Top 10 Rows Of The Data Set is ")
print(data.head(10))
print("The Last 10 Rows of The Data Sets is ")
print(data.tail(10))

# Dropping The Features Column From The Given Data Set is
cars = data.drop(columns=['feature_0','feature_1','feature_2','feature_3','feature_4','feature_5','feature_6','feature_7','feature_8','feature_9'], axis=1)
print("After The Unnecesary Columns Are ")
print(cars.head())

# Checking The Shape And Descriptions

print("The Shape of The Data Set is ")
print(data.shape)
print("the Description of The data Set is ")
print(data.describe())

print("The Column Name Are ")
print(data.columns)

print("The cars Data Type is")
print(data.dtypes)

# Checking The Null values in The COlummn Are
print("After Checking The Null values In The Given data Set is ")
print(data.isnull().sum())

cars = data.dropna()
print("The rows of The cars is ")
print(cars)
print(cars.isnull().sum())

# Calculate the age of the car

cars['age'] = 2020 - cars['year_produced']
print("After calculating The Age of The Car is ")
print(cars.head())

# All numeric (float and int) variables in the dataset
cars_numeric = cars.select_dtypes(include=['float64', 'int64'])
print(cars_numeric.head())

# Correlation matrix
cor = cars_numeric.corr()
print("The Correlation of The given data Set is ")
print(cor)

# Figure size
plt.figure(figsize=(16,8))

# Heatmap
sns.heatmap(cor, cmap="YlGnBu", annot=True)
plt.show()

# Visualizing The CateGorical values Of The Given Data Set is
plt.figure(figsize=(25, 6))

plt.subplot(1,3,1)
plt1 = cars.manufacturer_name.value_counts().plot(kind='bar')
plt.title('Companies Histogram')
plt1.set(xlabel = 'Car company', ylabel='Frequency of company')

plt.subplot(1,3,2)
plt1 = cars.body_type.value_counts().plot(kind='bar')
plt.title('Body Type')
plt1.set(xlabel = 'Body Type', ylabel='Frequency of Body Type')

plt.subplot(1,3,3)
plt1 = cars.engine_type.value_counts().plot(kind='bar')
plt.title('Engine Type Histogram')
plt1.set(xlabel = 'Engine Type', ylabel='Frequency of Engine type')

plt.show()

# When You Are going to Run The Above plot then You Will Saw that mostly
# Volkswagen is preferred than other cars.
# Sedan seems to be the popular type.
# Vehicles with gasoline are preffered.