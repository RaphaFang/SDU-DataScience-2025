from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import root_mean_squared_error

X = sales_df.drop("sales", axis=1).values
y = sales_df["sales"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

print(f"Predictions: {y_pred[:2]}, Actual Values: {y_test[:2]}")
# Predictions: [53176.66154234 70996.19873235], Actual Values: [55261.28 67574.9 ]

# ---------------------------------------------------------------------------
# r_squared and rmse
r_squared = reg.score(X_test, y_test)

rmse = root_mean_squared_error(y_test, y_pred)

print(f"R^2: {r_squared}, RMSE: {rmse}")
#  R^2: 0.9990165886162027, RMSE: 2942.372219812037

# ---------------------------------------------------------------------------
reg = LinearRegression()
kf = KFold(n_splits=6, shuffle=True, random_state=5)
cv_scores = cross_val_score(reg, X, y, cv=kf)

print(cv_scores)
# [0.74451678 0.77241887 0.76842114 0.7410406  0.75170022 0.74406484]

# ---------------------------------------------------------------------------
# mean
print(np.mean(cv_results))

# standard deviation
print(np.std(cv_results))

# 95% confidence interval
# 這邊會是單純看分布，不是計算信賴區間confidence interval
print(np.quantile(cv_results, [0.025, 0.975]))

# ---------------------------------------------------------------------------
from sklearn.linear_model import Ridge
alphas = [0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0]
ridge_scores = []
for alpha in alphas:
  ridge = Ridge(alpha=alpha)
  ridge.fit(X_train, y_train)
  score = ridge.score(X_test, y_test)
  ridge_scores.append(score)

print(ridge_scores)
# [0.9990152104759369, 0.9990152104759373, 0.9990152104759419, 0.999015210475987, 0.9990152104764387, 0.9990152104809561]

from sklearn.linear_model import RidgeCV
ridge_cv = RidgeCV(alphas=alphas, scoring="r2", cv=5)
ridge_cv.fit(X_train, y_train)
print(ridge_cv.alpha_)
# 10000.0

# ! 這組資料看起來沒差，可以推測這個係數縮小沒什麼差異

# ---------------------------------------------------------------------------
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

lasso = Lasso(0.3)
lasso.fit(X, y)

lasso_coef = lasso.coef_
print(lasso_coef)
# [ 3.56256962 -0.00397035  0.00496385]
# 重點在看他把不重要的壓縮到 0 。這邊只是單純看他會怎麼壓 coef，沒有特別要測量哪一個數值的影響，所以沒有跑 score()

plt.bar(sales_columns, lasso_coef)
plt.xticks(rotation=45)
plt.show()