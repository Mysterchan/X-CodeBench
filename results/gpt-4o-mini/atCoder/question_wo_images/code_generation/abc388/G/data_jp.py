def max_mirrors(N, A, Q, queries):
    results = []
    
    for L, R in queries:
        # Adjust for 0-indexing
        L -= 1
        R -= 1
        count = 0
        
        # Use a two-pointer technique to count possible pairs
        i, j = L, L
        
        while i <= R:
            while j <= R and A[j] <= 2 * A[i]:
                j += 1
            # Add the number of pairs that can be formed
            count += (j - i - 1) // 2
            i += 1
            
        results.append(count)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N + 1]))
Q = int(data[N + 1])
queries = []

for i in range(Q):
    L, R = int(data[N + 2 + 2 * i]), int(data[N + 2 + 2 * i + 1])
    queries.append((L, R))

# Solve the problem
answers = max_mirrors(N, A, Q, queries)

# Output results
for ans in answers:
    print(ans)