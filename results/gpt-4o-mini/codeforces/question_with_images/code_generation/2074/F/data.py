def min_quadtree_nodes(test_cases):
    results = []
    for l1, r1, l2, r2 in test_cases:
        # Calculate the width and height of the region
        width = r1 - l1
        height = r2 - l2
        
        # Calculate the number of leaf nodes needed
        # Each leaf node covers a 1x1 area
        num_nodes = (width * height)
        
        results.append(num_nodes)
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_quadtree_nodes(test_cases)

# Print results
for result in results:
    print(result)