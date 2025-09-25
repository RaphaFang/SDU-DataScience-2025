from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import Ridge
import pandas as pd



music_dummies = pd.get_dummies(music_df, drop_first=True)

# Print the new DataFrame's shape
print("Shape of music_dummies: {}".format(music_dummies.shape))

# Create X and y
X = music_dummies.drop('popularity', axis=1).values
y = music_dummies['popularity'].values

ridge = Ridge(0.2)

scores = cross_val_score(ridge, X, y, cv=kf, scoring="neg_mean_squared_error")
print(scores)
# [-68.49467657 -56.64985721 -70.89015472 -64.1558722  -80.14086371]

rmse = np.sqrt(-scores)
print(f"Average RMSE: {np.mean(rmse)}")
print(f"Standard Deviation of the target array: {np.std(y)}")
# Average RMSE: 8.2368538402023
# Standard Deviation of the target array: 14.02156909907019