import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_data)

plt.figure(figsize=(8, 4))
sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='cluster', palette='viridis', s=70)
plt.title("K-Means Clustering on Iris Dataset")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.histplot(df['sepal length (cm)'], bins=15, kde=True, color='coral')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.grid(True)
plt.tight_layout()
plt.show()
