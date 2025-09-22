# Perform the necessary imports
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pandas as pd

scaler = StandardScaler()
kmeans = KMeans(n_clusters=4)

pipeline = make_pipeline(scaler,kmeans)
pipeline.fit(samples)
labels = pipeline.predict(samples)

df = pd.DataFrame({'labels': labels, 'species': species})
ct = pd.crosstab(df['labels'], df['species'])

print(ct)


# ---------------------------------------------------------
from sklearn.preprocessing import Normalizer
import pandas as pd

normalizer = Normalizer()
kmeans = KMeans(n_clusters=10)

pipeline = make_pipeline(normalizer, kmeans)
pipeline.fit(movements)
labels = pipeline.predict(movements)

df = pd.DataFrame({'labels': labels, 'companies': companies})
df = df.sort_values('labels')

print(df)
