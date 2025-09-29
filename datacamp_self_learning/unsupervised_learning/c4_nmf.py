from sklearn.decomposition import NMF

model = NMF(6)
model.fit(articles)
nmf_features = model.transform(articles)

print(nmf_features.round(2)) # 這位產生一個大的不小於0具政

# ---------------------------------------------------------------------------
import pandas as pd

df = pd.DataFrame(nmf_features, index=titles) # 我覺得可以假設這邊的都是通過TfidfVectorizer 得到的文字轉數值

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
