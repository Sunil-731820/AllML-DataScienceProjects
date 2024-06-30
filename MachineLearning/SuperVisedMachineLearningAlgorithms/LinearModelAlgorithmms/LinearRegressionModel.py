from sklearn.linear_model import  LinearRegression

# Creating the Model
model = LinearRegression()

# fiiting the model on The basis of the Data Sets like Test And Train data

model.fit(X,y)


# After This predict The value for New input Data

model.predict(X_new_input_data)
