from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
import matplotlib.pyplot as plt
import numpy as np

X = churn_df.drop("churn", axis=1).values
y = churn_df["churn"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
# 0.8740629685157422

print(knn.score(X_train, y_train))
# 0.890847711927982

# ----------------------------------------------------------------------
# ! Overfitting and underfitting
neighbors = np.arange(1, 13)
train_accuracies = {}
test_accuracies = {}

for neighbor in neighbors:
  
	knn = KNeighborsClassifier(n_neighbors = neighbor)
	knn.fit(X_train, y_train)
  
	train_accuracies[neighbor] = knn.score(X_train, y_train)
	test_accuracies[neighbor] = knn.score(X_test, y_test)
	
print(neighbors, '\n', train_accuracies, '\n', test_accuracies)


plt.title("KNN: Varying Number of Neighbors")
plt.plot(neighbors, train_accuracies.values(),  label="Training Accuracy")
plt.plot(neighbors, test_accuracies.values(),  label="Testing Accuracy")
# 這邊順序有影響，測試下來，先提供 x 軸的數據，接著處理 y 軸

plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()