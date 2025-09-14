from sklearn.neighbors import KNeighborsClassifier 

churn_df = [[]] # 我拿不到資料

y = churn_df["churn"].values
X = churn_df[["account_length", "customer_service_calls"]].values  # ! 但是為什麼這邊都要轉 .value??
	# .values → 轉成 NumPy arr
	# Series → .values 變成 1D ndarray
	# DataFrame → .values 變成 2D ndarray

knn = KNeighborsClassifier(6)
knn.fit(X, y)

y_pred = knn.predict(X_new) # 這邊目的，透過新的 X_new ，推測基於這X會得到的y_pred，也就是模擬得到的流失率
print("Predictions: {}".format(y_pred)) 