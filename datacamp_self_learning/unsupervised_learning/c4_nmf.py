from sklearn.decomposition import NMF

model = NMF(6)
model.fit(articles)
nmf_features = model.transform(articles)

print(nmf_features.round(2)) # 這位產生一個大的不小於0具政

# ---------------------------------------------------------------------------
import pandas as pd

df = pd.DataFrame(nmf_features, index=titles) # 這邊是資料先跑過 NMF，會得到每一比資料對應到我設定的6欄位的關聯指數。塞進 df 只物欸了方便用 loc找東西

# print(df.head)
# HTTP 404                                       0.000  0.000e+00  0.000e+00  0.000e+00  0.000e+00  4.386e-01
# Alexa Internet                                 0.000  0.000e+00  0.000e+00  0.000e+00  0.000e+00  5.643e-01
# Internet Explorer                              0.004  0.000e+00  0.000e+00  0.000e+00  0.000e+00  3.970e-01

print(df.loc['Anne Hathaway'])
print(df.loc['Denzel Washington']) # 這邊可以不用在 .loc[] 裡面放入兩項 是因為這個 df 只有一個欄位

# ---------------------------------------------------------------------------
# NMF reconstruction
# 特徵是 [2, 1]，那麼重建方式就是：2 * row1, 1 * row2
# ---------------------------------------------------------------------------
import pandas as pd

components_df = pd.DataFrame(model.components_, columns=words)
print(components_df.shape) # (6, 13125)

component = components_df.iloc[3]
print(component.nlargest())
# film       0.632
# award      0.255
# starred    0.247
# role       0.213
# actress    0.188
# Name: 3, dtype: float64

# ---------------------------------------------------------------------------
# turn into digital image
from matplotlib import pyplot as plt

digit = samples[0,:]
# print(digit)
bitmap = digit.reshape(13,8)
# print(bitmap)

plt.imshow(bitmap, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()

# ---------------------------------------------------------------------------
from sklearn.decomposition import NMF

model = NMF(7)
features = model.fit_transform(samples)
digit_features = features[0,:]
print(digit_features)
# [2.57347960e-01 0.00000000e+00 0.00000000e+00 3.94333376e-01 3.64045642e-01 0.00000000e+00 3.51281573e-14]
for component in model.components_:
    show_as_image(component)


from sklearn.decomposition import PCA
model = PCA(7)
features = model.fit_transform(samples)
for component in model.components_:
    show_as_image(component)

# 這兩個差異在PCA做出來的會變紅色？
# show_as_image 這是dc 做出來的函數