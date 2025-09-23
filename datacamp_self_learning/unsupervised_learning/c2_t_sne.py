# 這是建立資料圖形的工具，類似之前的 kMean，但是不用自己調整 K 數量
# 不確保每次結果相同，且兩軸的數據也沒有意義。但可能每次會有大致的相對位置
# learning-rate要確定，全學習整張圖有可能灌滿

from sklearn.mainfold import TSNE
import matplotlib.pyplot as plt

model = TSNE(learning_rate=200)

tsne_features = model.fit_transform(samples)

xs = tsne_features[:,0]
ys = tsne_features[:,1]

plt.scatter(xs, ys, c=variety_numbers)
plt.show()

# ---------------------------------------------------------------------------
model = TSNE(learning_rate=50)
tsne_features = model.fit_transform(normalized_movements)

xs = tsne_features[:,0]
ys = tsne_features[:,1]
# companies 應該是從tsne_features獨立拉出來的欄位，只是他沒有讓我練習到

plt.scatter(xs, ys, alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
plt.show()
