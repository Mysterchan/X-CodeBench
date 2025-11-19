MOD = 998244353

def power(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result

def solve(N):
    if N == 1:
        return 1
    
    # 预计算组合数
    C = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
    
    # dp[i][j] = 大小为i和j的两部分的连通二分图数量
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i + j > N:
                break
            
            # 总的二分图数量（可以有边或没边）
            total = power(2, i * j, MOD)
            
            # 减去非连通的情况
            non_connected = 0
            for a in range(1, i):
                b = j  # 右侧全部
                # a个左侧顶点和b个右侧顶点连通，其余(i-a)个左侧顶点独立
                ways = (C[i][a] * dp[a][b]) % MOD
                non_connected = (non_connected + ways) % MOD
            
            for b in range(1, j):
                a = i  # 左侧全部
                ways = (C[j][b] * dp[a][b]) % MOD
                non_connected = (non_connected + ways) % MOD
            
            for a in range(1, i):
                for b in range(1, j):
                    ways = (C[i][a] * C[j][b]) % MOD
                    ways = (ways * dp[a][b]) % MOD
                    ways = (ways * power(2, (i-a)*(j-b), MOD)) % MOD
                    non_connected = (non_connected + ways) % MOD
            
            dp[i][j] = (total - non_connected + MOD) % MOD
    
    # 计算答案：枚举所有可能的二分划分
    ans = 0
    for k in range(1, N):
        # 选择k个顶点作为一部分，N-k个作为另一部分
        # 由于二分图两部分是对称的，当k != N-k时需要除以2
        ways = (C[N][k] * dp[k][N-k]) % MOD
        if k != N - k:
            ways = (ways * power(2, MOD - 2, MOD)) % MOD  # 除以2
        ans = (ans + ways) % MOD
    
    return ans

N = int(input())
print(solve(N))