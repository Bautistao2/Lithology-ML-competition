import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.kmeans_clustering_pipeline import load_data, preprocess_data, train_kmeans, plot_clusters
from src.utils import calculate_silhouette
from src.config import DATA_PATH, N_CLUSTERS

# Load and preprocess data
data = load_data(DATA_PATH)
if data is not None:
    scaled_data = preprocess_data(data, data.columns)

    # Train K-Means model
    kmeans, labels = train_kmeans(scaled_data, N_CLUSTERS)

    # Save results
    data['Cluster'] = labels
    data.to_csv("data_with_clusters.csv", index=False)

    # Visualize clusters (if 2D)
    if scaled_data.shape[1] == 2:
        plot_clusters(scaled_data, labels, kmeans)

    # Calculate silhouette score
    score = calculate_silhouette(scaled_data, labels)
    print(f"Silhouette Score: {score}")
