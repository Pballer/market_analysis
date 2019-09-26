from sklearn.cluster import KMeans

def find_optimal_k(max_k=6):
    """Find optimal k based on silhouette score."""
    sil_scores = {}
    for i in tqdm(range(2, max_k)):
        k_means = KMeans(n_clusters=i)
        k_means.fit(X)
        y_hat = k_means.predict(X)
        labels = k_means.labels_
        silhouette = silhouette_score(X, labels)
    return silhouette

def add_label(data, optimal_k):
    """Add roi label."""
    k_means = KMeans(n_clusters=3, random_state=23)
    k_means.fit(X)
    y_hat = k_means.predict(X)
    labels = k_means.labels_
    data['roi_class'] = labels

if __name__ == '__main__':
    sil_scores = find_optimal_k(data, 6)
    print(sorted(sil_scores.items(), key=lambda x: x[1], reverse=True))
