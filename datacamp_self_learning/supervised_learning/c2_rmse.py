from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

X = sales_df.drop("sales", axis=1).values
y = sales_df["sales"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

print(f"Predictions: {y_pred[:2]}, Actual Values: {y_test[:2]}")

# ---------------------------------------------------------------------------
# r_squared and rmse
r_squared = reg.score(X_test, y_test)

rmse = root_mean_squared_error(y_test, y_pred)

print(f"R^2: {r_squared}, RMSE: {rmse}")
#  R^2: 0.9990165886162027, RMSE: 2942.372219812037

# ---------------------------------------------------------------------------
