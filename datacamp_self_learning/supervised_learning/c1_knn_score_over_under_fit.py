from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
import matplotlib.pyplot as plt
import numpy as np

X = churn_df.drop("churn", axis=1).values
y = churn_df["churn"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
knn = KNeighborsClassifier(n_neighbors=5)
# 這邊設定 stratify ，是因為 我們要穩定住即便是隨機的測試數據，也要讓他這20%的資料比例如同原先數據
# 但前提是，他要是二元資料，以及，他確實比例極端，例如1:9 才要特別調者個 stratify

knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
# 0.8740629685157422

print(knn.score(X_train, y_train))
# 0.890847711927982

# ----------------------------------------------------------------------
# ! k too small -> Overfitting, k too big -> Underfitting
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

# ----------------------------------------------------------------------
# find the actual K
from sklearn.model_selection import cross_val_score
import numpy as np

k_range = range(1, 30)
cv_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy')
    cv_scores.append(float(scores.mean()))
print(f"k = {np.argmax(cv_scores) + 1}, score = {cv_scores[np.argmax(cv_scores)]}")
# k = 10, score = 0.8559273182957392