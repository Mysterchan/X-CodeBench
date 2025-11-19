N = int(input())
C = [input() for _ in range(N)]

inf = float('inf')
A = [[inf] * N for _ in range(N)]

# Initialize the distances for direct edges and self-loops
for i in range(N):
    A[i][i] = 0
    for j in range(N):
        if C[i][j] != '-':
            A[i][j] = 1

# Floyd-Warshall-like approach to find shortest palindromic paths
for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][k] < inf and A[k][j] < inf:
                # Check if we can form a palindrome
                if C[k][i] != '-' and C[j][k] != '-' and C[k][i] == C[j][k]:
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])

# Replace inf with -1 for output
for i in range(N):
    for j in range(N):
        if A[i][j] == inf:
            A[i][j] = -1
    print(*A[i])