import  pandas as pd
import numpy as np
import sqlite3
# Reading The JSON data is

data = pd.read_json("EmployeeData.json")
print("The JSOn data is ")
print(data)



# Reading The Data From THE dataBase
# Creating the connections database and Pycharm
# con = sqlite3.connect("agentdatabase.db")
# df = pd.read_sql_query("select *from agent",con)
# print("The Data Frame is ")
# print(df)
#
