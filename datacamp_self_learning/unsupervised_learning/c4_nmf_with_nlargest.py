import pandas as pd
from sklearn.preprocessing import normalize

norm_features = normalize(nmf_features)
df = pd.DataFrame(norm_features, index=titles)

article = df.loc['Cristiano Ronaldo']
similarities = df.dot(article) # 拿 df 裡 每一篇文章的向量，和 article 做內積，一路到資料表走完

print(similarities.nlargest())
    # Cristiano Ronaldo                1.0
    # Franck Ribéry                    1.0
    # Radamel Falcao                   1.0
    # Zlatan Ibrahimović               1.0
    # France national football team    1.0
    # dtype: float64
top5 = similarities.drop('Cristiano Ronaldo').nlargest(5) # 也可以這樣作

# ---------------------------------------------------------------------------
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

scaler = MaxAbsScaler()
nmf = NMF(20)
normalizer = Normalizer()
pipeline = make_pipeline(scaler, nmf, normalizer)

norm_features = pipeline.fit_transform(artists)

# ---------------------------------------------------------------------------
df = pd.DataFrame(norm_features, index=artist_names)

artist = df.loc['Bruce Springsteen']
similarities = df.dot(artist)
print(similarities.nlargest())
# Bruce Springsteen    1.000
# Neil Young           0.952
# Leonard Cohen        0.893
# Bob Dylan            0.813
# Van Morrison         0.809