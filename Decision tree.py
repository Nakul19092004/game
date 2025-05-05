import math 
 
# Tennis data (Outlook, Temp, Humidity, Wind, PlayTennis) 
data = [ 
    ['Sunny', 'Hot', 'High', 'Weak', 'No'], 
    ['Sunny', 'Hot', 'High', 'Strong', 'No'], 
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'], 
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'], 
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'], 
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'], 
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'], 
    ['Sunny', 'Mild', 'High', 'Weak', 'No'], 
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'], 
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'], 
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'], 
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'], 
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'], 
    ['Rain', 'Mild', 'High', 'Strong', 'No'] 
] 
 
features = ['Outlook', 'Temp', 'Humidity', 'Wind'] 
 
def entropy(values): 
    counts = {} 
    for v in values: 
        counts[v] = counts.get(v, 0) + 1 
    return -sum((count/len(values)) * math.log2(count/len(values))  
            for count in counts.values()) 
 
def best_feature(data, features): 
    base_entropy = entropy([row[-1] for row in data]) 
    best_gain = 0 
    best_feat = None 
     
    for i in range(len(features)): 
        feat_values = {row[i] for row in data} 
        feat_entropy = 0 
        for value in feat_values: 
            subset = [row[-1] for row in data if row[i] == value] 
            feat_entropy += (len(subset)/len(data)) * entropy(subset) 
        gain = base_entropy - feat_entropy 
        if gain > best_gain: 
            best_gain = gain 
            best_feat = i 
    return best_feat 
 
def build_tree(data, features): 
    outcomes = [row[-1] for row in data] 
    if len(set(outcomes)) == 1: 
        return outcomes[0] 
     
    best_idx = best_feature(data, features) 
    if best_idx is None: 
        return max(set(outcomes), key=outcomes.count) 
     
    tree = {features[best_idx]: {}} 
    for value in {row[best_idx] for row in data}: 
        subset = [row for row in data if row[best_idx] == value] 
        tree[features[best_idx]][value] = build_tree(subset, features) 
    return tree 
 
tree = build_tree(data, features) 
print(tree) 
