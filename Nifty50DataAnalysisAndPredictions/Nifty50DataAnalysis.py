import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Path to the Excel file
file_path = "D:\\DataSets\\Nift50.xlsx"

# Read the Excel file
df = pd.read_excel(file_path)

print(df.head(10))

print("The Siz of The data Set is :")
print(df.shape)

# Combine datasets vertically (concatenate along rows)
# combined_dataset = pd.concat(file_path, ignore_index=True)
# 1. Ranking overall, by Industry, and by single title (top 5), using mean Volume (and Trades)

# Group by Industry
industry_ranking = df.groupby('Series').agg({'Volume': 'mean', 'Trades': 'mean'}).sort_values(by='Volume', ascending=False).head(5)
# Plotting
industry_ranking.plot(kind='bar', y=['Volume', 'Trades'], title='Top 5 Series by Mean Volume and Trades')

plt.show()

since_inception_ranking = df.groupby('Symbol').agg({'Trades': ['mean', 'sum']}).sort_values(by=('Trades', 'sum'), ascending=False).head(5)

# Plotting
since_inception_ranking.plot(kind='bar', y=('Trades', 'sum'), title='Top 5 Tickers by Sum of Trades Since Inception')

plt.show()

df['Date'] = pd.to_datetime(df['Date'])
price_change = df.groupby('Symbol')['Close'].agg(['first', 'last'])
price_change['delta_percentage'] = ((price_change['last'] - price_change['first']) / price_change['first']) * 100
best_stocks = price_change.sort_values(by='delta_percentage', ascending=False).head(5)

# Plotting
best_stocks.plot(kind='bar', y='delta_percentage', title='Top 5 Stocks by Delta Price % Since Inception')
plt.show()

worst_stocks = price_change.sort_values(by='delta_percentage').head(5)

# Plotting
worst_stocks.plot(kind='bar', y='delta_percentage', title='Top 5 Stocks by Delta Price % Since Inception')
plt.show()

std_deviation = df.groupby('Symbol')['Close'].std()
mean_prices = df.groupby('Symbol')['Close'].mean()
coefficient_of_variation = std_deviation / mean_prices

# Plotting
coefficient_of_variation.plot(kind='bar', title='Coefficient of Variation for Each Stock')
plt.show()