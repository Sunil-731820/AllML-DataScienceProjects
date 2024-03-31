import pandas as pd
import  numpy as np
info = pd.DataFrame([
    [1,5,6],
    [10,12,15],
    [18,21,24],
    [np.nan,np.nan,np.nan]
],columns=["FirstColumn","SecondColumn","ThirdColumn"])
print("The Given Data Frame is ")
print(info)

print("The Sum of The Column Wise Is ")
print(info.agg(['sum']))

print("The Minimum Values of The Column Wise is ")
print(info.agg(['min']))

info1 = pd.DataFrame([
    [1,5,7],
    [10,12,15],
    [18,21,24],
    [np.nan,np.nan,np.nan]
],columns=["FirstColumn","SecondColumn","ThirdColumn"])
print('The Second Data Frame Is ')
print(info1)
print(info1.agg({'FirstColumn':['sum','min'],'SecondColumn':['min','max']}))

