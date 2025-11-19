def max_beauty(test_cases):
    results = []
    
    for n, k, parents in test_cases:
        # Create a list to store the count of leaves for each node
        children_count = [0] * (n + 1)
        
        for p in parents:
            children_count[p] += 1
        
        # Count leaves in the tree
        leaves = sum(1 for count in children_count[1:] if count == 0)
        
        # Calculate the maximum beauty
        if leaves <= k:  # If we can label all leaves with 0
            beauty = leaves
        else:  # Otherwise, label k leaves with 0
            beauty = k
        
        results.append(beauty)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

# Prepare test cases
t = int(data[0])
test_cases = []
index = 1
for _ in range(t):
    n, k = map(int, data[index].split())
    parents = list(map(int, data[index + 1].split()))
    test_cases.append((n, k, parents))
    index += 2

# Get the results
results = max_beauty(test_cases)

# Print results
for result in results:
    print(result)