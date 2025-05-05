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
 
# Names for points 
names = ['s1', 's2', 's3', 's4', 's5', 's6'] 
 
# Euclidean distance function 
def euclidean(p1, p2): 
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) 
 
# Linkage distance calculation 
def cluster_distance(c1, c2, method): 
    distances = [euclidean(data[i], data[j]) for i in c1 for j in c2] 
    if method == 'single': 
        return min(distances) 
    elif method == 'complete': 
        return max(distances) 
    elif method == 'average': 
        return sum(distances) / len(distances) 
 
# Agglomerative clustering 
def agglomerative_clustering(data, names, linkage='single'): 
    clusters = [[i] for i in range(len(data))] 
     
    print(f"Initial Clusters ({linkage} linkage):") 
    for i, cluster in enumerate(clusters): 
        print(f"Cluster {i+1}: {[names[idx] for idx in cluster]}") 
    print() 
 
    while len(clusters) > 1: 
        min_dist = float('inf') 
        pair = (0, 1) 
 
        # Find closest pair 
        for i in range(len(clusters)): 
            for j in range(i+1, len(clusters)): 
                dist = cluster_distance(clusters[i], clusters[j], linkage) 
                if dist < min_dist: 
                    min_dist = dist 
                    pair = (i, j) 
 
        # Merge clusters 
        i, j = pair 
        clusters[i] += clusters[j] 
        clusters.pop(j) 
 
        # Print current clusters 
        print(f"After merging clusters {i+1} and {j+1}:") 
        for k, cluster in enumerate(clusters): 
            print(f"Cluster {k+1}: {[names[idx] for idx in cluster]}") 
        print() 
 
    return [names[i] for i in clusters[0]] 
 
# Run for all linkage methods 
print("\n=== SINGLE LINKAGE ===\n") 
agglomerative_clustering(data, names, linkage='single') 
 
print("\n=== COMPLETE LINKAGE ===\n") 
agglomerative_clustering(data, names, linkage='complete') 
 
print("\n=== AVERAGE LINKAGE ===\n") 
agglomerative_clustering(data, names, linkage='average')
