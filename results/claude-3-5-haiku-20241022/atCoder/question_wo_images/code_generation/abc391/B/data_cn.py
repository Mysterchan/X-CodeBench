N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(M)]

for a in range(1, N - M + 2):
    for b in range(1, N - M + 2):
        match = True
        for i in range(M):
            for j in range(M):
                if S[a + i - 1][b + j - 1] != T[i][j]:
                    match = False
                    break
            if not match:
                break
        if match:
            print(a, b)
            break
    if match:
        break