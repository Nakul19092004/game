# Transactions 
data = [ 
    ['Bread', 'Butter', 'Jam', 'Milk'], 
    ['Bread', 'Butter', 'Milk'], 
    ['Bread', 'Juice', 'Cereal'], 
    ['Bread', 'Milk', 'Juice'], 
    ['Butter', 'Milk', 'Juice'] 
] 
 
support_percent = 50 
confidence_percent = 75 
total = len(data) 
 
# Get unique items 
items = [] 
for t in data: 
    for item in t: 
        if item not in items: 
            items.append(item) 
 
# Count support 
def count(items_list): 
    c = 0 
    for t in data: 
        if all(i in t for i in items_list): 
            c += 1 
    return c 
 
# Check 2-item combinations 
for i in range(len(items)): 
    for j in range(i + 1, len(items)): 
        A = items[i] 
        B = items[j] 
        ab = count([A, B]) 
        support = (ab / total) * 100 
 
        if support >= support_percent: 
            a = count([A]) 
            b = count([B]) 
            conf_ab = (ab / a) * 100 
            conf_ba = (ab / b) * 100 
 
            if conf_ab >= confidence_percent: 
                print(f"conf({A} -> {B}) = {ab}/{a} = {round(conf_ab)}%") 
 
            if conf_ba >= confidence_percent: 
                print(f"conf({B} -> {A}) = {ab}/{b} = {round(conf_ba)}%")
