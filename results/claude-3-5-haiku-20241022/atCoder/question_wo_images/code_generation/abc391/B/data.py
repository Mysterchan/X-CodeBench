N, M = map(int, input().split())

S = []
for i in range(N):
    S.append(input().strip())

T = []
for i in range(M):
    T.append(input().strip())

# Try all possible positions (a, b)
for a in range(1, N - M + 2):
    for b in range(1, N - M + 2):
        # Check if T matches the subgrid of S starting at (a, b)
        match = True
        for i in range(1, M + 1):
            for j in range(1, M + 1):
                if S[a + i - 2][b + j - 2] != T[i - 1][j - 1]:
                    match = False
                    break
            if not match:
                break
        
        if match:
            print(a, b)
            exit()