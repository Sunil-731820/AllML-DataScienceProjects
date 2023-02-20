import  pandas as pd
info1 = pd.DataFrame({"x":[25,15,12,19]})
print("The data Frame Is ")
print(info1)

info2 = pd.DataFrame({"x":[25,15,12],
                      "y":[47,24,17],
                      "z":[38,12,45]
                      })
print("The Second Data Frame Is ")
print(info2)
print("After appending The One Data Frame into the Other Dataframe ")
print(info1.append(info2,ignore_index=True,sort=False))


