def min_operations(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        total_zeros_needed = 0
        total_ones_needed = 0
        total_zeros_available = 0
        total_ones_available = 0
        
        for j in range(n):
            a, b, c, d = test_cases[i][1][j]
            # Current and target state differences
            total_zeros_available += a
            total_ones_available += b
            total_zeros_needed += c
            total_ones_needed += d
        
        # We need to move the excess to meet the needs
        excess_zeros = max(0, total_zeros_available - total_zeros_needed)
        excess_ones = max(0, total_ones_available - total_ones_needed)
        
        # Minimum operations will be the maximum of the excess counts
        results.append(max(excess_zeros, excess_ones))
    
    return results

# Read input
input_data = input().splitlines()
t = int(input_data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(input_data[index])
    piles = []
    for j in range(n):
        a, b, c, d = map(int, input_data[index + j + 1].split())
        piles.append((a, b, c, d))
    test_cases.append((n, piles))
    index += n + 1

# Get results
results = min_operations(t, test_cases)

# Print results
for result in results:
    print(result)