import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate some data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Fit K-means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Get cluster centers
centers = kmeans.cluster_centers_

# Get cluster labels
labels = kmeans.labels_

# Plot the data and the cluster centroids
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.show()