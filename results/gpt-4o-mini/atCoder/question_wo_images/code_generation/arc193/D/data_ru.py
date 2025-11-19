def min_operations_to_match(T, test_cases):
    results = []
    
    for case in test_cases:
        N, A, B = case
        a_positions = []
        b_positions = []
        
        # Collect positions of 1s in A and B
        for i in range(N):
            if A[i] == '1':
                a_positions.append(i)
            if B[i] == '1':
                b_positions.append(i)
        
        # If there are no positions in A or B, it's impossible
        if not a_positions or not b_positions:
            results.append(-1)
            continue
        
        # Check if we can match B with A
        a_index = 0
        b_index = 0
        operations = 0
        possible = True
        
        while b_index < len(b_positions):
            if a_index < len(a_positions) and a_positions[a_index] < b_positions[b_index]:
                # Move to the next A position
                a_index += 1
            elif a_index < len(a_positions) and a_positions[a_index] == b_positions[b_index]:
                # Match found, move both indices
                a_index += 1
                b_index += 1
            else:
                # We need to move A positions to the right
                if a_index == 0 or a_positions[a_index - 1] < b_positions[b_index]:
                    # Calculate the number of operations needed
                    operations += b_positions[b_index] - a_positions[a_index - 1]
                    b_index += 1
                else:
                    possible = False
                    break
        
        if possible:
            results.append(operations)
        else:
            results.append(-1)
    
    return results

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

results = min_operations_to_match(T, test_cases)
for result in results:
    print(result)