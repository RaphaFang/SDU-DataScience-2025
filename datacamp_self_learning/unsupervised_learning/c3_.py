from sklearn.decomposition import PCA
pca = PCA(2)
pca_features= pca.fit_transform(scaled_samples)

print(pca_features.shape) # (85, 2)

# ---------------------------------------------------------------------------
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer() 
csr_mat = tfidf.fit_transform(documents)
# print(documents) # ['cats say meow', 'dogs say woof', 'dogs chase cats']
print(csr_mat.toarray())
# [[0.51785612 0.         0.         0.68091856 0.51785612 0.        ]
#  [0.         0.         0.51785612 0.         0.51785612 0.68091856]
#  [0.51785612 0.68091856 0.51785612 0.         0.         0.        ]]

words = tfidf.get_feature_names_out()
print(words) #  ['cats' 'chase' 'dogs' 'meow' 'say' 'woof']

# ---------------------------------------------------------------------------
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
import pandas as pd

svd = TruncatedSVD(50)
kmeans = KMeans(6)
pipeline = make_pipeline(svd,kmeans)
pipeline.fit(articles)
labels = pipeline.predict(articles)

df = pd.DataFrame({'label': labels, 'article': titles})

print(df.sort_values('label'))

