MOD = 998244353

def solve():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    
    Q, sh, sw = map(int, input().split())
    sh -= 1
    sw -= 1
    
    for _ in range(Q):
        line = input().split()
        d = line[0]
        a = int(line[1])
        
        if d == 'L':
            sw -= 1
        elif d == 'R':
            sw += 1
        elif d == 'U':
            sh -= 1
        elif d == 'D':
            sh += 1
        
        A[sh][sw] = a
        
        dp = [[0] * W for _ in range(H)]
        dp[0][0] = A[0][0]
        
        for h in range(H):
            for w in range(W):
                if h == 0 and w == 0:
                    continue
                val = 0
                if h > 0:
                    val = (val + dp[h-1][w]) % MOD
                if w > 0:
                    val = (val + dp[h][w-1]) % MOD
                dp[h][w] = (val * A[h][w]) % MOD
        
        print(dp[H-1][W-1])

solve()