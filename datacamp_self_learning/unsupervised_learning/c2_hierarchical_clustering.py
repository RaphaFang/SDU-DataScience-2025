# Hierarchical clustering

from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib .pyplot as plt

mergings = linkage(samples, method='complete')

dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()

# ---------------------------------------------------------------------------
from sklearn.preprocessing import normalize

normalized_movements = normalize(movements)
mergings = linkage(normalized_movements, method='complete')

dendrogram(mergings,
    labels=companies,
    leaf_rotation=90,
    leaf_font_size=6,
)
plt.show()

# ---------------------------------------------------------------------------
import pandas as pd
from scipy.cluster.hierarchy import fcluster

labels = fcluster(mergings,t=6,criterion='distance')

df = pd.DataFrame({'labels': labels, 'varieties': varieties})

ct = pd.crosstab(df['labels'], df['varieties'])
print(ct)
    # varieties  Canadian wheat  Kama wheat  Rosa wheat
    # labels                                           
    # 1                      14           3           0
    # 2                       0           0          14
    # 3                       0          11           0