def solve():
    N, M = map(int, input().split())
    S = input().strip()
    
    MOD = 998244353
    
    # dp[i][j][k] = i文字目まで見て、Sのj文字目まで使って、LCSがkである文字列の数
    # でも、「LCSがちょうどk」ではなく「LCSが最大k」で計算して後で差分を取る
    
    # より良いアプローチ: dp[i][j] = i文字目まで見て、Sのj文字目までマッチした文字列の数
    # これを使ってLCSがちょうどkになる数を計算
    
    # dp[i][j][exactly_k] の代わりに、
    # dp[i][j] = LCSがちょうどjである、i文字の文字列の数
    
    # 新しいアプローチ: 
    # dp[m][n][lcs] = 長さmの文字列で、Sの最初のn文字を考慮して、LCSがlcsである数
    
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(M + 1)]
    dp[0][0][0] = 1
    
    for i in range(M + 1):
        for j in range(N + 1):
            for k in range(N + 1):
                if dp[i][j][k] == 0:
                    continue
                if i == M:
                    continue
                
                # 次の文字を追加
                for c in range(26):
                    ch = chr(ord('a') + c)
                    # Sのj文字目以降で最初にchが現れる位置を探す
                    next_j = -1
                    for jj in range(j, N):
                        if S[jj] == ch:
                            next_j = jj + 1
                            break
                    
                    if next_j == -1:
                        # マッチしない
                        dp[i + 1][j][k] = (dp[i + 1][j][k] + dp[i][j][k]) % MOD
                    else:
                        # マッチする
                        dp[i + 1][next_j][k + 1] = (dp[i + 1][next_j][k + 1] + dp[i][j][k]) % MOD
    
    # 答えを集計
    ans = [0] * (N + 1)
    for j in range(N + 1):
        for k in range(N + 1):
            ans[k] = (ans[k] + dp[M][j][k]) % MOD
    
    print(' '.join(map(str, ans)))

solve()