from sklearn.linear_model import LogisticRegression

x = [[1,2],[2,3],[3,4],[4,5],[5,6]]
y = [0,0,1,1,1]

# Training The Model using fit Method

model = LogisticRegression()
model.fit(x,y)

# Making the Prediction
prediction = model.predict([[15,86]])[0]

print("The Value of the prediction is : =")
print(prediction)
