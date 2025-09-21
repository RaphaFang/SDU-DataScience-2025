from sklearn.linear_model import LinearRegression
import numpy as np

X = sales_df['radio'].values
y = sales_df['sales'].values

X = X.reshape(-1, 1)
print(X.shape, y.shape)


reg = LinearRegression()
reg.fit(X, y)
predictions = reg.predict(X)

print(predictions[:5])
# [ 95491.17119147 117829.51038393 173423.38071499 291603.11444202 111137.28167129]