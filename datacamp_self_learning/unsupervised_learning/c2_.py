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
