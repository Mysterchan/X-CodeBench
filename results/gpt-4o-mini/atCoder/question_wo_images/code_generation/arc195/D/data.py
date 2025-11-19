def min_operations_to_empty_sequence(test_cases):
    results = []
    
    for A in test_cases:
        n = len(A)
        operations = 0
        
        # Count the number of segments of equal elements
        segments = 1  # At least one segment exists
        for i in range(1, n):
            if A[i] != A[i - 1]:
                segments += 1
        
        # The minimum operations required is the number of segments + (number of segments - 1)
        # The first segment can be removed directly, and each subsequent segment requires a swap
        operations = segments + (segments - 1)
        
        results.append(operations)
    
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
test_cases = []

index = 1
for _ in range(T):
    N = int(data[index])
    A = list(map(int, data[index + 1].split()))
    test_cases.append(A)
    index += 2

results = min_operations_to_empty_sequence(test_cases)
print('\n'.join(map(str, results)))