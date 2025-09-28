# PCA 的主要目的是 找到最大化變異的方向，同時 消除特徵間的相關性
# 我的理解是找到分叉最大的那一欄位，接著第二與第一正交，也就是讓二者相乘會等於0，一路作到最後一筆
# 因為讓所有欄位都正交，也就讓彼此 uncorrelated 了。不會因為部分欄位correlated，例如身高體重這兩比資料其實有很高相關性
# 簡單來說，我是把多col「降維」了

# principal components 一定會是兩軸，一軸指向橢圓形長邊，一軸指向短邊，呈現90度角

# intrinsic dimension: is the number of PCA features with significant variance
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

width = grains[:,0]
length = grains[:,1]

plt.scatter(width, length)
plt.axis('equal')
plt.show()

correlation, pvalue = pearsonr(width,length) # 皮爾森係數，1 完全相關，0 完全不相關，-1 完全負相關 
print(correlation) # 0.860414937714347

# ---------------------------------------------------------------------------
from sklearn.decomposition import PCA

model = PCA()
pca_features = model.fit_transform(grains)

xs = pca_features[:,0]
ys = pca_features[:,1]

plt.scatter(xs, ys)
plt.axis('equal')
plt.show()

correlation, pvalue = pearsonr(xs, ys)
print(correlation) # 2.2870594307278225e-14

# ---------------------------------------------------------------------------
plt.scatter(grains[:,0], grains[:,1])

model = PCA()
model.fit(grains)

mean = model.mean_
first_pc = model.components_[0,:]

plt.arrow(mean[0], mean[1], first_pc[0], first_pc[1], color='red', width=0.01)
plt.axis('equal')
plt.show()

# ---------------------------------------------------------------------------
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

scaler = StandardScaler()
pca = PCA()
pipeline = make_pipeline(scaler, pca)
pipeline.fit(samples)

features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_)  
# features 這邊就是 range(0,6)
# [3.94616746e+00 1.78097907e+00 2.43235593e-01 1.00351845e-01 5.63140996e-04 1.31462706e-04]
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(features)
plt.show()

# ---------------------------------------------------------------------------