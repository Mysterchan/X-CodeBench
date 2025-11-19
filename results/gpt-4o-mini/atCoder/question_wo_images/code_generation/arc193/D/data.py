def min_operations_to_match(T, test_cases):
    results = []
    
    for case in test_cases:
        N, A, B = case
        pieces = []
        required = []
        
        # Collect positions of pieces in A and required positions in B
        for i in range(N):
            if A[i] == '1':
                pieces.append(i)
            if B[i] == '1':
                required.append(i)
        
        # If the number of pieces is less than required positions, it's impossible
        if len(pieces) < len(required):
            results.append(-1)
            continue
        
        # Calculate the minimum number of operations needed
        operations = 0
        possible = True
        
        for req_index in range(len(required)):
            if req_index >= len(pieces):
                possible = False
                break
            
            # Calculate the distance to move the piece to the required position
            operations += abs(pieces[req_index] - required[req_index])
        
        if possible:
            results.append(operations)
        else:
            results.append(-1)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []

index = 1
for _ in range(T):
    N = int(data[index])
    A = data[index + 1]
    B = data[index + 2]
    test_cases.append((N, A, B))
    index += 3

# Get results
results = min_operations_to_match(T, test_cases)

# Print results
for result in results:
    print(result)