import polars as pl

data = {"col1": [1, 2], "col2": [3, 4]}
print("The data is : =")
print(data)
df3 = pl.DataFrame(data, schema=[("col1", pl.Float32), ("col2", pl.Int64)])
print("The dataFrame is : =")
print(df3)
