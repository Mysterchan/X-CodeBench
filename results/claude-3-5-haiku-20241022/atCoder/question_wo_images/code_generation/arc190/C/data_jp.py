MOD = 998244353

def solve():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    
    Q, sh, sw = map(int, input().split())
    sh -= 1
    sw -= 1
    
    # dp[i][j] = sum of products of all paths from (0,0) to (i,j)
    def compute_answer():
        dp = [[0] * W for _ in range(H)]
        dp[0][0] = A[0][0]
        
        for i in range(H):
            for j in range(W):
                if i == 0 and j == 0:
                    continue
                val = 0
                if i > 0:
                    val = (val + dp[i-1][j]) % MOD
                if j > 0:
                    val = (val + dp[i][j-1]) % MOD
                dp[i][j] = (val * A[i][j]) % MOD
        
        return dp[H-1][W-1]
    
    for _ in range(Q):
        d, a = input().split()
        a = int(a)
        
        if d == 'L':
            sw -= 1
        elif d == 'R':
            sw += 1
        elif d == 'U':
            sh -= 1
        elif d == 'D':
            sh += 1
        
        A[sh][sw] = a
        print(compute_answer())

solve()