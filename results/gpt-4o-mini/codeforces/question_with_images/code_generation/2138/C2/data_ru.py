def max_beauty_in_tree(test_cases):
    results = []
    
    for n, k, parents in test_cases:
        # Create adjacency list for the tree
        tree = [[] for _ in range(n + 1)]
        for child in range(2, n + 1):
            tree[parents[child - 2]].append(child)

        # Count leaves and their contribution to the beauty
        leaves = 0
        max_beauty = 0
        
        # This will hold the number of children at each node
        children_count = [0] * (n + 1)
        
        # Count leaves and prepare to calculate contribution
        for node in range(1, n + 1):
            children_count[parents[node - 2]] += (1 if node > 1 else 0)

        # Counting leaves based on children
        for node in range(1, n + 1):
            if children_count[node] == 0:  # It's a leaf
                leaves += 1

        # Beauty calculation
        free_zeros = k
        free_ones = n - k
        
        # Maximum beauty is limited by number of leaves and the availability of zeros and ones
        if free_zeros >= leaves:
            max_beauty = leaves  # we can assign a zero to all leaves
        else:
            max_beauty = free_zeros + min(leaves - free_zeros, free_ones)

        results.append(max_beauty)

    return results


# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1
test_cases = []

for _ in range(t):
    n, k = map(int, data[index].split())
    index += 1
    if n > 2:
        parents = list(map(int, data[index].split()))
    else:
        parents = []
    
    test_cases.append((n, k, parents))
    index += 1

# Getting results
results = max_beauty_in_tree(test_cases)

# Output results
for result in results:
    print(result)