def find_grid(S, T, N, M):
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
                return a + 1, b + 1  # converting to 1-based indexing

import sys
input = sys.stdin.read

data = input().strip().split()
N = int(data[0])
M = int(data[1])
S = [data[i + 2] for i in range(N)]
T = [data[N + 2 + i] for i in range(M)]

a, b = find_grid(S, T, N, M)
print(a, b)