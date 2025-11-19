def minimize_dissatisfaction(T, test_cases):
    results = []
    
    for case in test_cases:
        N, intervals = case
        people = sorted(range(N), key=lambda i: (intervals[i][0], intervals[i][1]))
        
        # Initialize the result permutation
        P = [0] * N
        
        # Assign seats based on sorted order
        for i in range(N):
            P[people[i]] = i + 1
        
        results.append(P)
    
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
    intervals = []
    for i in range(N):
        L, R = map(int, data[index + 1 + i].split())
        intervals.append((L, R))
    test_cases.append((N, intervals))
    index += N + 1

# Get results
results = minimize_dissatisfaction(T, test_cases)

# Print results
for result in results:
    print(" ".join(map(str, result)))