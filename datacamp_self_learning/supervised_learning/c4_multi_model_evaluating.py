from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score, KFold
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, Lasso, LinearRegression, Ridge, DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import root_mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer


models = {"Linear Regression": LinearRegression(), "Ridge": Ridge(alpha=0.1), "Lasso": Lasso(alpha=0.1)}
results = []

# Loop through the models' values
for model in models.values():
  kf = KFold(n_splits=6, random_state=42, shuffle=True)
  
  # Perform cross-validation
  cv_scores = cross_val_score(model, X_train, y_train, cv=kf)
  
  # Append the results
  results.append(cv_scores)

# Create a box plot of the results
plt.boxplot(results, labels=models.keys())
plt.show()

# ------------------------------------------------------------------------
for name, model in models.items():
  # Fit the model to the training data
  model.fit(X_train_scaled, y_train)
  
  # Make predictions on the test set
  y_pred = model.predict(X_test_scaled)
  
  test_rmse = root_mean_squared_error(y_test, y_pred)
  print("{} Test Set RMSE: {}".format(name, test_rmse))
print(np.std(y_test))
# Linear Regression Test Set RMSE: 0.1198885150594757
# Ridge Test Set RMSE: 0.11987066103299669
# std: 0.20994576616399305

# 好像還是要學 nRMSE 可以看到比例，多少趴出錯

# ------------------------------------------------------------------------
models = {"Logistic Regression": LogisticRegression(), "KNN": KNeighborsClassifier(), "Decision Tree Classifier": DecisionTreeClassifier()}
results = []

for model in models.values():
  kf = KFold(n_splits=6, random_state=12, shuffle=True)
  cv_results = cross_val_score(model, X_train_scaled, y_train, cv=kf)
  results.append(cv_results)

plt.boxplot(results, labels=models.keys())
plt.show()

# ------------------------------------------------------------------------
steps = [("imp_mean", SimpleImputer()), 
         ("scaler", StandardScaler()), 
         ("logreg", LogisticRegression())]

pipeline = Pipeline(steps)
params = {"logreg__solver": ["newton-cg", "saga", "lbfgs"],
         "logreg__C": np.linspace(0.001, 1.0, 10)}

tuning = GridSearchCV(pipeline, param_grid=params)
tuning.fit(X_train, y_train)
y_pred = tuning.predict(X_test) # 這邊會是 0101 也就是真實預估的

print(tuning.best_params_, tuning.best_score_)
# best_params_: {'logreg__C': np.float64(0.112), 'logreg__solver': 'newton-cg'}
# best_score_: 0.8453333333333333
# 這個出來還是在fold裡面模擬的東西

# 理論上最後還要檢查 tuning.score(X_test, y_test)
# 0.82
# 因為這才是真實的模擬
