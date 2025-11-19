def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    E = [tuple(map(int, input().split())) for _ in range(M)]
    
    ans = 0
    Adj = [[0] * N for _ in range(N)]
    for u, v in E:
        u -= 1
        v -= 1
        Adj[u][v] += 1
        Adj[v][u] += 1

    for i in range(N):
        for j in range(i + 1, N):
            ans += Adj[i][j] * (Adj[i][j] - 1) // 2

    cnt = 0
    dp = [[0] * N for _ in range(1 << N)]
    for i in range(N):
        dp[1 << i][i] = 1
    
    for st in range(1, 1 << N):
        b = (st & -st).bit_length() - 1

        for u in range(b, N):
            if (st >> u) & 1 and dp[st][u] > 0:
                for v in range(b, N):
                    if not ((st >> v) & 1):
                        if Adj[u][v] > 0:
                            nst = st | (1 << v)
                            dp[nst][v] += dp[st][u] * Adj[u][v]
    
    for st in range(1, 1 << N):
        if bin(st).count('1') < 3:
            continue
        
        b = (st & -st).bit_length() - 1        
        for u in range(b + 1, N):
            if (st >> u) & 1:
                if Adj[u][b] > 0:
                    cnt += dp[st][u] * Adj[u][b]
    ans += cnt // 2

    print(ans)


if __name__ == '__main__':
    main()
