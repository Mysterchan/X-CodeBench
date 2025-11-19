import sys
from collections import Counter
from math import gcd
from functools import reduce

def max_gcd_with_k_elements(N, K, A):
    # Count occurrences of each number in the array
    count = Counter(A)
    max_number = max(A)
    results = []
    
    for i in range(N):
        ai = A[i]
        max_gcd = 0
        
        # Start with multiples of A[i]
        for m in range(ai, max_number + 1, ai):
            if m in count:
                top_k_elements = count[m]
                # Find out how many more we need to pick from other multiples
                remaining_k = K - (1 if m == ai else 0)
                
                if remaining_k <= 0:
                    max_gcd = max(max_gcd, m)
                    continue
                
                # Include all multiples of m
                total_count = 0
                for multiple in range(m, max_number + 1, m):
                    if multiple in count:
                        total_count += count[multiple]
                
                # If we can pick enough elements
                if total_count >= K:
                    max_gcd = max(max_gcd, m)
        
        results.append(max_gcd)

    return results

# Reading input
input_data = sys.stdin.read().split()
N = int(input_data[0])
K = int(input_data[1])
A = list(map(int, input_data[2:N + 2]))

# Calculate results
results = max_gcd_with_k_elements(N, K, A)

# Print results
for res in results:
    print(res)