from collections import deque

N = int(input())
C = [input() for _ in range(N)]

inf = 10**10
A = [[inf]*N for _ in range(N)]

# Initialize: distance 0 for same vertex
for i in range(N):
    A[i][i] = 0

# BFS for each starting configuration
# State: (distance, start_vertex, end_vertex)
q = deque()

# Add all initial states (distance 0 for i==j, distance 1 for single edges)
for i in range(N):
    q.append((0, i, i))
    
for i in range(N):
    for j in range(N):
        if i != j and C[i][j] != '-':
            if A[i][j] > 1:
                A[i][j] = 1
                q.append((1, i, j))

visited = set()

while q:
    dist, i, j = q.popleft()
    
    if (i, j) in visited:
        continue
    
    # Only mark as visited if this is the optimal distance
    if dist > A[i][j]:
        continue
        
    visited.add((i, j))
    
    # Try to extend palindrome by adding matching edges at both ends
    for s in range(N):
        if C[s][i] == '-':
            continue
        cs = C[s][i]
        
        for t in range(N):
            if C[j][t] == '-':
                continue
            ct = C[j][t]
            
            if cs != ct:
                continue
            
            new_dist = dist + 2
            
            if new_dist < A[s][t]:
                A[s][t] = new_dist
                q.append((new_dist, s, t))

# Output
for i in range(N):
    row = []
    for j in range(N):
        if A[i][j] == inf:
            row.append(-1)
        else:
            row.append(A[i][j])
    print(*row)