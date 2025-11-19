def find_submatrix(N, M, S, T):
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
                return a + 1, b + 1  # Convert to 1-based index
    return None

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
S = data[1:N + 1]
T = data[N + 1:N + 1 + M]

# Find the submatrix and output the result
result = find_submatrix(N, M, S, T)
if result:
    print(result[0], result[1])