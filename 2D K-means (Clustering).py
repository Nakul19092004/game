# Sample data: (Age, Amount) 
data = [ 
    (20, 500),   # c1 
    (40, 1000),  # c2 
    (30, 800),   # c3 
    (18, 300),   # c4 
    (28, 1200),  # c5 
    (35, 1400),  # c6 
    (45, 1800)   # c7 
] 
 
# Initial centroids (first two points) 
centroids = [data[0], data[1]]  # (20, 500) and (40, 1000) 
 
def euclidean_distance(p1, p2): 
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5 
 
def k_means_single_iteration(data, centroids): 
    # Step 1: Create empty clusters 
    clusters = [[] for _ in range(len(centroids))] 
     
    # Step 2: Assign each point to the nearest centroid 
    for point in data: 
        distances = [euclidean_distance(point, centroid) for centroid in 
centroids] 
        closest = distances.index(min(distances))  # Find the closest centroid 
        clusters[closest].append(point)  # Assign point to that cluster 
     
    return centroids, clusters 
 
# Run K-Means for just one iteration 
centroids, clusters = k_means_single_iteration(data, centroids) 
 
# Output the results 
print("Centroids:", centroids) 
for i, cluster in enumerate(clusters): 
    print(f"Cluster {i + 1}: {cluster}") 
