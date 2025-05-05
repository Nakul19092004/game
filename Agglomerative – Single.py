import math 
 
# Data: (X, Y) 
data = [ 
    (4, 3),  # s1 
    (1, 4),  # s2 
    (2, 1),  # s3 
    (3, 8),  # s4 
    (6, 9),  # s5 
    (5, 1),  # s6 
] 
 
# Names for the points 
names = ['s1', 's2', 's3', 's4', 's5', 's6'] 
 
# Function to calculate Euclidean distance 
def euclidean_distance(p1, p2): 
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) 
 
# Agglomerative clustering (single linkage) 
def agglomerative_clustering(data, names): 
    clusters = [[i] for i in range(len(data))]  # Each point starts as its own cluster
     
    # Print initial clusters 
    print("Initial Clusters:") 
    for i, cluster in enumerate(clusters): 
        cluster_names = [names[idx] for idx in cluster] 
        print(f"Cluster {i + 1}: {cluster_names}") 
    print() 
 
    while len(clusters) > 1: 
        min_dist = float('inf') 
        closest_pair = None 
         
        # Find the closest pair of clusters 
        for i in range(len(clusters)): 
            for j in range(i + 1, len(clusters)): 
                # Find minimum distance between any two points in the clusters (single linkage) 
                dist = min([euclidean_distance(data[p1], data[p2]) for p1 in clusters[i] for p2 in clusters[j]]) 
                 
                if dist < min_dist: 
                    min_dist = dist 
                    closest_pair = (i, j) 
         
        # Merge the closest clusters 
        c1, c2 = closest_pair 
        clusters[c1] += clusters[c2] 
        clusters.pop(c2) 
 
        # Print the current clusters after merging 
        print(f"After merging clusters {c1 + 1} and {c2 + 1}:") 
        for i, cluster in enumerate(clusters): 
            cluster_names = [names[idx] for idx in cluster] 
            print(f"Cluster {i + 1}: {cluster_names}") 
        print() 
 
    # Return the final clusters with names 
    final_cluster = clusters[0] 
    return [names[i] for i in final_cluster] 
 
# Run the agglomerative clustering 
final_clusters = agglomerative_clustering(data, names)
