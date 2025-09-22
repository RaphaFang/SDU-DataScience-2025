from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

samples = [] # 遺憾我拿不到資料，他是一個numpy arr
ks = range(1, 6) # 當然這邊可以設定成很大，會呈現一個log曲線
inertias = []

for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(samples)
    inertias.append(model.inertia_)
    
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()