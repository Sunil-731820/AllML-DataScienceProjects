import  numpy as np
import pandas as pd

reading_Data = pd.read_csv("covid19DataAnanlysis.csv")
print("The Data is ")
print(reading_Data)

# Coverting this data to the DataFrame using pandas
df = pd.DataFrame(reading_Data)
print("The DataFame is ")
print(df)

# The Head & tail of THe Data is
print("The Head Of The Data is ")
print(df.head(10))
print("The Tail of The Data is ")
print(df.tail(10))

# The Sample Of The Data is
print("The Sample Data is ")
print(df.sample(n=10))

# The Country value count is
print("The Country value Count is ")
print(df["country"].value_counts())
print("The Death value Count is ")
print(df["indicator"].value_counts())
print("The Length of The Data Frame is ")
print(len(df))

# Cases OverAll
lastWeekCases = df.loc[df['year_week']=='2022-47'].loc[df['indicator']=='cases']
print("The Last Week cases is ")
print(lastWeekCases)

# Death OverAll is

lastWeekDeath = df.loc[df['year_week']=='2022-47'].loc[df['indicator']=='deaths']
print("The Over All Death is ")
print(lastWeekDeath)

# Ploting The Data In The Graph

import matplotlib
import matplotlib.pyplot as plt
#  1: COuntry name : EU/EEA (total) to see all Cases WIth Death rayets During The covid 19 cases
euCases = df.loc[df['country']=='EU/EEA (total)'].loc[df['indicator']=='cases']
euDeaths = df.loc[df['country']=='EU/EEA (total)'].loc[df['indicator']=='deaths']
fig, ax = plt.subplots(figsize=(15,8))
euDeaths['weekly_count'] = euDeaths['weekly_count']*100
ax.plot(euCases['year_week'], euCases['weekly_count'], label='Cases EU', color='black' )
ax.plot(euDeaths['year_week'], euDeaths['weekly_count'], label='Deaths EU', color='red')
ax.legend()
plt.show()

#  2: Country name is : germany to see all The Case With The daeath rates During Covid 19 cases
germanyCases = df.loc[df['country']=='Germany'].loc[df['indicator']=='cases']
germanyDeaths = df.loc[df['country']=='Germany'].loc[df['indicator']=='deaths']
fig1 , ax1 = plt.subplots(figsize=(15,8)) #Not Required here
germanyDeaths["weekly_count"] = germanyDeaths["weekly_count"]*100
ax1.plot(germanyCases["year_week"],germanyCases["weekly_count"],label="Cases in Germany", color="black")
ax1.plot(germanyDeaths["year_week"],germanyDeaths["weekly_count"],label="death In Germany",color="red")
ax1.legend()
plt.show()








