def find_pattern(N, M, S, T):
    for a in range(N - M + 1):
        for b in range(N - M + 1):
            match = True
            for i in range(M):
                for j in range(M):
                    if S[a + i][b + j] != T[i][j]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return a + 1, b + 1  # Convert to 1-based indexing

# Read input
N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(M)]

# Find the matching pattern
result = find_pattern(N, M, S, T)

# Print the result
print(result[0], result[1])