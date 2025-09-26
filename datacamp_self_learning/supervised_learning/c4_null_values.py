import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import confusion_matrix, classification_report


# print(music_df.isna().sum().sort_values())

music_df = music_df.dropna(subset=["genre", "popularity", "loudness", "liveness", "tempo"])
music_df["genre"] = np.where(music_df["genre"] == "Rock", 1, 0)
# pd.get_dummies()會更好處理多cata情況，但是這邊只要處理是否是 Rock ，所以這樣也行

print(music_df.isna().sum().sort_values())
print("Shape of the `music_df`: {}".format(music_df.shape))


imputer = SimpleImputer()
knn = KNeighborsClassifier(3)
steps = [("imputer", imputer), 
         ("knn", knn)]

pipeline = Pipeline(steps)
pipeline.fit(X_train,y_train)
y_pred = pipeline.predict(X_test)

print(confusion_matrix(y_test, y_pred))