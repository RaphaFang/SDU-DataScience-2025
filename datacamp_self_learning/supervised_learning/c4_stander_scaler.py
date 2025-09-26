from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, Lasso
import numpy as np
# prevent data leakage
# 要注意即便是 train_test_split 也要在 standerlize 之前做到。
# 不然你是用已經影響到的資料，來訓練以及檢查。很有可能透過 整體平均 來補上洞，這樣就洩漏答案了
# 目標洩漏 (Target leakage)
# 資料前處理洩漏 (Preprocessing leakage)


steps = [("scaler", StandardScaler()),
         ("lasso", Lasso(alpha=0.5))]

pipeline = Pipeline(steps)
pipeline.fit(X_train, y_train)
print(pipeline.score(X_test, y_test))
# 0.6193523316282489

# ------------------------------------------------------------------------
steps = [("scaler", StandardScaler()),
         ("logreg", LogisticRegression())]
pipeline = Pipeline(steps)

parameters = {"logreg__C": np.linspace(0.001, 1.0, 20)}
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=21)

cv = GridSearchCV(pipeline, param_grid=parameters)
cv.fit(X_train, y_train)

print(cv.best_score_, cv.best_params_)
# cv.best_score_: 0.8412499999999999
# cv.best_params_: 0.1061578947368421

# 下面的分數會高，可以看成因為有調參數