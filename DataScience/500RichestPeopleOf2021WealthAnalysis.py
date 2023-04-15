import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("500RichestPeople2021.csv")
print(data)

print("The Top 10 rows of The Data Set is ")
print(data.head(10))

print("The Last 10 values of The data From The Given Data Set is ")
print(data.tail(10))

print("The Info Of The data Set is ")
print(data.info)
print("The Use of The Describe() is ")
print(data.describe())
fig= plt.figure(figsize=(6,6))
nameOfPerson=data["Name"][:10]
print("The Name of the person is ")
print(nameOfPerson)
netWorthOfPerson = data["Total Net Worth"][:10]
print("The Net Worth Of The person is ")
print(netWorthOfPerson)
plt.plot(nameOfPerson,netWorthOfPerson)
plt.xlabel("Name Of The Person is ")
plt.ylabel("The Net Worth of The person is ")
plt.show()

fig= plt.figure(figsize=(6,6))

top10_person=data[:10]
print("The top 10 person Data is ")
print(top10_person)
plt.plot(nameOfPerson,netWorthOfPerson)

plt.title("Top 10 Rich People and Their Net Worth(WorldWide)",fontsize=20,fontweight='bold')
plt.ylabel("Name",fontsize=20,fontweight='bold')
plt.xlabel("Total Net Worth(billion $)",fontsize=20,fontweight='bold')
plt.show()

