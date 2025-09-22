from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

model = KMeans(n_clusters=3)
labels = model.fit_predict(samples)

df = pd.DataFrame()
ct = pd.crosstab(df['labels'], df['varieties'])

print(ct)


# varieties  Canadian wheat  Kama wheat  Rosa wheat
# labels                                           
# 0                      68           9           0
# 1                       0           1          60
# 2                       2          60          10