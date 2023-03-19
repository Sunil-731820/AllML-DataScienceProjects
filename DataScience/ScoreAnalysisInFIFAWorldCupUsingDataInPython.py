import matplotlib
import  numpy as np
import pandas as pd
import  matplotlib
import  matplotlib.pyplot as plt

# First Step To read The Data From Any FIles
readingDataFromCSVFile = pd.read_csv("WorldCupData.csv")
print("The data After Reading From The CSV FIle Is ")
print(readingDataFromCSVFile)
print("getting The Information regarding The Given CSV data ")
print(readingDataFromCSVFile.info)

# Printing The Some Head values using head()
print("The Top 10 values is ")
print(readingDataFromCSVFile.head(10))

# Getting Some Sample using sample(n=10)
print("The Some Sample Values From The data is ")
print(readingDataFromCSVFile.sample(n=10))

teams = np.unique(readingDataFromCSVFile[["teamA","teamB"]].values)
print("The Total Number of The  Teams is ")
print(teams)
print("The length of The Team is ")
print(len(teams))
gameCounter = {}
for team in teams:
    if team in readingDataFromCSVFile["teamA"].unique():
        countTeamA = (readingDataFromCSVFile.teamA == team).sum()
    if(team in readingDataFromCSVFile["teamB"].unique()):
        countTeamB = (readingDataFromCSVFile.teamB == team).sum()
    countOverAll = countTeamA+ countTeamB
    gameCounter.update({team:countOverAll})
# gameCounter = dict(sorted(gameCounter.items(),key=lambda ))
gameCounterList = list(gameCounter.items())
print("The game Counter List is ")
print(gameCounterList)
# print(gameCounterList[-15:])

# plt.bar(*zip(*gameCounter.items()))
plt.bar(*zip(*gameCounterList[:]))
plt.xticks(rotation=90)
plt.show()

# Now Making The Winner Values
# If Team A = team & Winner = Team A --> +3 if draw --> +1
# # If Team B = team & Winner = Team B --> +3 if draw --> +1
goalCounter = {}
for team in teams:
    if team in readingDataFromCSVFile["teamA"].unique():
        goalsTeamA = readingDataFromCSVFile.loc[readingDataFromCSVFile["teamA"]==team,"goalsA"].sum()
    if team in readingDataFromCSVFile["teamB"].unique():
        goalsTeamB = readingDataFromCSVFile.loc[readingDataFromCSVFile["teamB"]==team,'goalsB'].sum()
    goalsOverAll = goalsTeamA + goalsTeamB
    goalCounter.update({team:goalsOverAll})
# goalCounter = dict(sorted(goalCounter.items(),key=lambda items))
goalCounter = list(goalCounter.items())
print("The Goal Counter Is ")
print(goalCounter)
print(goalCounter[:])

# Plotting The Goal COunter Using MatPlotlib
plt.bar(*zip(*goalCounter[-15:]))
plt.xticks(rotation=90)
plt.show()


pointsTeamA = 0
for entry in readingDataFromCSVFile.loc[readingDataFromCSVFile['teamA']=="Germany","winner"]:
    if entry=="teamA":
        pointsTeamA +=3
    if entry=="draw":
        pointsTeamA +=1
    print(entry)
print("The Point table For The Team A  Is ")
print(pointsTeamA)

# Similary The PointCounter for The Both Team is

pointCounter = {}
for team in teams:
    if team in readingDataFromCSVFile["teamA"].unique():
        pointsTeamA = 0
        for entry in readingDataFromCSVFile.loc[readingDataFromCSVFile["teamA"]==team,"winner"]:
            if entry == "teamA":
                pointsTeamA += 3
            if entry=="draw":
                pointsTeamA += 1
    if team in readingDataFromCSVFile["teamB"].unique():
        pointsTeamB = 0
        for entry in readingDataFromCSVFile.loc[readingDataFromCSVFile["teamB"]==team,"winner"]:
            if entry=="teamB":
                pointsTeamB +=3
            if entry == "draw":
                pointsTeamB +=1
    pointsOverAll = pointsTeamA + pointsTeamB
    pointCounter.update({team:pointsOverAll})

print("The Point COunter is ")
print(pointCounter)

# Plotting The Given Points Data is
pointCounter = list(pointCounter.items())
plt.bar(*zip(*pointCounter[:]))
plt.xticks(rotation=90)
plt.show()

