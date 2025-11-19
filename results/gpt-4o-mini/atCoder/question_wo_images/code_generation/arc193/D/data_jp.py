def min_moves_to_match(T, test_cases):
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
        
        # If the number of 1s in A and B are not the same, it's impossible
        if len(a_positions) != len(b_positions):
            results.append(-1)
            continue
        
        # Calculate the minimum moves required
        moves = 0
        for a, b in zip(a_positions, b_positions):
            moves += abs(a - b)
        
        results.append(moves)
    
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

results = min_moves_to_match(T, test_cases)
print('\n'.join(map(str, results)))