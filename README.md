K-means clustering is a popular unsupervised machine learning algorithm used to divide a dataset into `k` non-overlapping subgroups based on feature similarity. This example demonstrates the following:

- Generating synthetic data using `make_blobs`.
- Performing K-means clustering with `scikit-learn`.
- Visualizing the clustered data and centroids.

## Prerequisites

To run this example, you need to have the following libraries installed:

- `numpy`
- `matplotlib`
- `scikit-learn`

You can install these dependencies using `pip`:

```sh
pip install numpy matplotlib scikit-learn
```

**Code Explanation**

The kmeans_clustering.py file contains the code for generating data, performing K-means clustering, and visualizing the results. Here's a brief overview of the code:

**Data Generation:**

Using make_blobs from scikit-learn.datasets to generate synthetic data with 4 centers.

**K-means Clustering:**

Using KMeans from scikit-learn.cluster to fit the K-means model to the data.

**Plotting:**

Using matplotlib.pyplot to create a scatter plot of the data points and the cluster centroids.
