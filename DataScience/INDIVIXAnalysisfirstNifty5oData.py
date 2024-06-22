import  numpy as np
import pandas as pd

# loading The Data from The CSV Files

indivix = pd.read_csv("INDIAVIX.csv")
print("The Data is ")
print(indivix)

print("The Head of the top 10 rows are ")
print(indivix.head(10))

print("Checking The Last 10 rows ")
print(indivix.tail())

# Replacing the Nan value with zero because index started

indivix.fillna(0,inplace=True)
print("Now After Setting The zero values In Place of Nan values Now The top 10 values is ")
print(indivix.head(10))

# Dropping The open , High , And Low values

indivix.drop(['Open',"High","Low"],inplace=True,axis=1)

print("After Dropping the columns values from The CSV Files ")
print(indivix.head(10))


# Now I have Started My Analysis on The Nifty 50 Data Analysis parts

loadingThedataOfNifty50 = pd.read_csv("NIFTY 50.csv")
print("AFter Loading The data is ")
print(loadingThedataOfNifty50)
print("Displaying the data of the top 10 rows from The Nifty 50 parts ")
print(loadingThedataOfNifty50.head(10))

print("Displaying The last 10 rows of The data from The Nifty50 is ")
print(loadingThedataOfNifty50.tail(10))


#droping open high low and divyield%
loadingThedataOfNifty50.drop(['Open','High','Low','Div Yield %'],axis=1,inplace=True)
print("After Dropping The Columns the Data is : ")
print(loadingThedataOfNifty50)
print(loadingThedataOfNifty50.head(10))

print("the Description of The data is ")

print(loadingThedataOfNifty50.describe())

loadingThedataOfNifty50['Date'] = loadingThedataOfNifty50['Date'].str.replace('-', '')
print("After Replacing The Data of the - With Blank ")
print(loadingThedataOfNifty50)

print(loadingThedataOfNifty50['Date'])

print("The top 10 value is ")
print(loadingThedataOfNifty50.head(10))

# Its time to Plot the data on The Graph
import matplotlib.pyplot as plt
import seaborn as sns
date = loadingThedataOfNifty50['Date']
close = loadingThedataOfNifty50['Close']

plt.plot(date,close)
plt.title('Plot of Specific Column')  # Set the title of the plot
plt.xlabel('date')  # Set the label for the x-axis
plt.ylabel('close')  # Set the label for the y-axis
plt.grid(True)  # Enable grid lines
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Ad

plt.show()

sns.lmplot(x='Date',y='Close',data=loadingThedataOfNifty50)



