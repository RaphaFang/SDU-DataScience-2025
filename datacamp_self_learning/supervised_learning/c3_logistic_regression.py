# Accuracy = 打中的總體比例（正確率）。
# Precision = 當你說「這是靶心」時，有幾成真的在靶心。「模型預測的可靠性」
# Recall = 真正的靶心裡，有幾成被你找到。「模型找出所有正樣本的能力」

from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=6)
model = knn.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
# [[116  35]
#  [ 46  34]]

#               precision    recall  f1-score   support

#            0       0.72      0.77      0.74       151
#            1       0.49      0.42      0.46        80

#     accuracy                           0.65       231
#    macro avg       0.60      0.60      0.60       231
# weighted avg       0.64      0.65      0.64       231

# ---------------------------------------------------------------------------
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred_probs = logreg.predict_proba(X_test)[:,1]

print(y_pred_probs[:10])

# class 0 通常當作 negative（負類）第0 col
# class 1 通常當作 positive（正類）第1 col
# 而我們在意的是positive的機率，所以只要調用出第二欄的機率就好

# ----------------------------------------------------------------------
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

fpr, tpr, thresholds = roc_curve(y_test, y_pred_probs)

plt.plot([0, 1], [0, 1], 'k--') # 這是先定義x y 兩邊的定義，以及畫出點狀斜線

plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate') # FPR 這是真的抓錯的機率
plt.ylabel('True Positive Rate') # TPR 這就是Recall，也就是真的對並且有抓出來
plt.title('ROC Curve for Diabetes Prediction')
plt.show()

# ----------------------------------------------------------------------
from sklearn.metrics import roc_auc_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print(roc_auc_score(y_test, y_pred_probs)) # 要記得這邊的應該要是prediction 因為roc related 是要看機率的
# 0.8002483443708608

# ----------------------------------------------------------------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import numpy as np

param_grid = {"alpha": np.linspace(0.00001, 1, 20)}
lasso_cv = GridSearchCV(lasso, param_grid, cv=kf)
lasso_cv.fit(X_train, y_train)

print("Tuned lasso paramaters: {}".format(lasso_cv.best_params_))
print("Tuned lasso score: {}".format(lasso_cv.best_score_))


params = {"penalty": ["l1", "l2"],
         "tol": np.linspace(0.0001, 1.0, 50),
         "C": np.linspace(0.1, 1.0, 50),
         "class_weight": ["balanced", {0:0.8, 1:0.2}]}
logreg_cv = RandomizedSearchCV(logreg, params, cv=kf)
logreg_cv.fit(X_train, y_train)

print(f"best_params_: {format(logreg_cv.best_params_)}")
print(f"best_score_: {format(logreg_cv.best_score_)}")
# best_params_: {'tol': np.float64(0.3878163265306122), 'penalty': 'l2', 'class_weight': {0: 0.8, 1: 0.2}, 'C': np.float64(0.46734693877551026)}
# best_score_: 0.6465946954551512


# ----------------------------------------------------------------------
# np.arange(start, stop, step)
# np.linspace(start, stop, slice_time) num這邊表示切幾次

# 這邊寫的方式是一次處理兩個penalty，所以兩者會用同樣solver。
# 但，不是每個 solver 都支援所有 penalty，所以會建議寫成下面
    # params = [
    #     {
    #         "penalty": ["l2"],
    #         "solver": ["lbfgs", "saga"],
    #         "C": np.linspace(0.1, 1.0, 50),
    #         "tol": np.linspace(0.0001, 1.0, 50),
    #         "class_weight": ["balanced", {0:0.8, 1:0.2}]
    #     },
    #     {
    #         "penalty": ["l1"],
    #         "solver": ["saga"],   # 只允許 saga
    #         "C": np.linspace(0.1, 1.0, 50),
    #         "tol": np.linspace(0.0001, 1.0, 50),
    #         "class_weight": ["balanced", {0:0.8, 1:0.2}]
    #     }
    # ]