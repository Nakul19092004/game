 # FP-tree node class

class FPTreeNode:

    def __init__(self, item, count, parent):

        self.item = item

        self.count = count

        self.parent = parent

        self.children = {}



# Sample transactions

transactions = [

    ['bread', 'milk'],

    ['bread', 'diaper', 'beer', 'egg'],

    ['milk', 'diaper', 'beer', 'cola'],

    ['bread', 'milk', 'diaper', 'beer'],

    ['bread', 'milk', 'diaper', 'cola']

]



min_support = 2



# Step 1: Count item frequencies

item_counts = {}

for txn in transactions:

    for item in txn:

        item_counts[item] = item_counts.get(item, 0) + 1



# Step 2: Remove infrequent items and sort by frequency

items = {item for item, count in item_counts.items() if count >= min_support}



def sort_transaction(txn):

    return sorted([item for item in txn if item in items], key=lambda x: -item_counts[x])



# Step 3: Build FP-Tree

root = FPTreeNode(None, 1, None)



for txn in transactions:

    sorted_items = sort_transaction(txn)

    current_node = root

    for item in sorted_items:

        if item in current_node.children:

            current_node.children[item].count += 1

        else:

            current_node.children[item] = FPTreeNode(item, 1, current_node)

        current_node = current_node.children[item]



# Helper: Print FP-Tree

def print_tree(node, indent=0):

    for child in node.children.values():

        print(' ' * indent + f"{child.item} ({child.count})")

        print_tree(child, indent + 1)



print("FP-Tree Structure:")

print_tree(root)
