MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def solve(H, W, C):
    # 最後の操作で塗られたマスの集合がグリッド全体を覆う必要がある
    # 最後の操作で選ばれたマスの位置を(r, c)とすると、
    # 行rと列cが塗られる
    
    # dp[i][j] = i行j列まで考えたときの場合の数
    # 各マスについて、そのマスが「最後に塗られた操作」を決める
    
    # 別のアプローチ: 各マスが最後にどの操作で塗られたかを考える
    # 最後の操作の集合は、すべてのマスをカバーする必要がある
    
    # より簡潔なアプローチ:
    # f[i][j] = i行j列まで全て塗られている場合の数
    # ただし、行0からi-1、列0からj-1が全て塗られている状態
    
    # 包除原理を使う
    # 全体 - (少なくとも1行が塗られていない) + (少なくとも2行が塗られていない) - ...
    
    # dp[r][c] = r行、c列がすべて塗られている場合の数
    # 最後の操作がどこかによって場合分け
    
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][0] = 1
    
    # 前計算: 階乗とその逆元
    fact = [1] * (H + W + 1)
    for i in range(1, H + W + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (H + W + 1)
    inv_fact[H + W] = modinv(fact[H + W])
    for i in range(H + W - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    
    for r in range(H + 1):
        for c in range(W + 1):
            if r == 0 and c == 0:
                continue
            
            # (r, c)を塗るために必要な操作の場合の数
            val = 0
            
            # 最後の操作が行rを選ぶ場合
            if r > 0:
                # 行rを選んで、列0からc-1がすべてカバーされる
                # つまり、列0からc-1のいずれかで行rを選ぶ
                # c通りの選び方、各選び方でC色
                val += dp[r-1][c] * c % MOD * C % MOD
            
            # 最後の操作が列cを選ぶ場合
            if c > 0:
                # 列cを選んで、行0からr-1がすべてカバーされる
                # r通りの選び方、各選び方でC色
                val += dp[r][c-1] * r % MOD * C % MOD
            
            # 両方を引きすぎたので戻す
            if r > 0 and c > 0:
                # (r, c)を選ぶ場合
                val -= dp[r-1][c-1] * C % MOD
            
            dp[r][c] = val % MOD
    
    print(dp[H][W])

H, W, C = map(int, input().split())
solve(H, W, C)