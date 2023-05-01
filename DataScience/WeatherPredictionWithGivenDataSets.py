import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Reading The Given Data Sets
data = pd.read_csv("seattle-weather.csv")
print("The Data Set is ")
print(data)

# The Top 10 data From The Data Set is
print("The Top 10 data set is ")
print(data.head(10))

# The Last 10 Data from The data Set is
print("The last 10 data from The Data Set is ")
print(data.tail(10))

# Check The Null Values In The Column of The Given data Set
print("Counting The Number of The Null values In The Column")
print(data.isnull().sum())

# printing The Date Column From The Given Data Set
print("The date Column is ")
date = data["date"]
print(date)

print("The precipitation COlumn is ")
precipitation = data["precipitation"]
print(precipitation)



# Plotting The Graph Between Date and precipitation
plt.plot(date,precipitation)
plt.show()

#convert the data type into datetime
data["date"] = pd.to_datetime(data["date"])
print(data.nunique())

# Now Plotting The Grapch Using Counter plot in seaborn
plt.figure(figsize=(10,5))
sns.countplot(x = 'weather',data = data,palette="ch:start=.2,rot=-.3")
plt.xlabel("weather",fontweight='bold',size=13)
plt.ylabel("Count",fontweight='bold',size=13)
plt.show()

plt.figure(figsize=(18,8))
sns.set_theme()
sns.lineplot(x = 'date',y='temp_max',data=data)
plt.xlabel("Date",fontweight='bold',size=13)
plt.ylabel("Temp_Max",fontweight='bold',size=13)
plt.show()

plt.figure(figsize=(18,8))
sns.set_theme()
sns.lineplot(x = 'date',y='temp_min',data=data)
plt.xlabel("Date",fontweight='bold',size=13)
plt.ylabel("Temp_Min",fontweight='bold',size=13)
plt.show()

plt.figure(figsize=(18,8))
sns.set_theme()
sns.lineplot(x = 'date',y='wind',data=data)
plt.xlabel("Date",fontweight='bold',size=13)
plt.ylabel("wind",fontweight='bold',size=13)
plt.show()

plt.figure(figsize=(14,8))
sns.pairplot(data.drop('date',axis=1),hue='weather',palette="YlOrBr")
plt.show()

plt.figure(figsize=(10,5))
sns.catplot(x='weather',y ='temp_min',data=data,palette = "RdBu")
plt.show()

plt.figure(figsize=(10,5))
sns.catplot(x='weather',y ='wind',data=data,palette = "magma")
plt.show()

sns.catplot(x='weather',y ='precipitation',data=data,palette = "viridis")
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(18, 10))

fig.suptitle('Price Range vs all numerical factor')

sns.scatterplot(ax=axes[0, 0], data=data, x='weather', y='precipitation')
sns.scatterplot(ax=axes[0, 1], data=data, x='weather', y='temp_max')
sns.scatterplot(ax=axes[1, 0], data=data, x='weather', y='temp_min')
sns.scatterplot(ax=axes[1, 1], data=data, x='weather', y='wind')
plt.show()