import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("kc_house_data.csv")

# Selecting interested columns
columns = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'price']

df = df.loc[:, columns]
df.head(10)

# Arrange data into features and target
features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors']

X = df.loc[:, features]
Y = df.loc[:, ['price']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, train_size = .75)

# Creating and Training a model with Scikit-Learn
reg = DecisionTreeRegressor(max_depth= 2, random_state=0)
reg.fit(X_train, Y_train)

# Predict multiple observations
reg.predict(X_test[0:10])

X_test.head(1)

# Predict 1 observation
reg.predict(X_test.iloc[0].values.reshape(1,-1))

# Find the coefficient of determination of the prediction
score = reg.score(X_test, Y_test)
print(score)
