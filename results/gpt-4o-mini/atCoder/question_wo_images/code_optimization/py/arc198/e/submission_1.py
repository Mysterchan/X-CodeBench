MOD = 998244353

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    
    MAX = 1 << N
    dp = [0] * (MAX + 1)
    dp[0] = 1

    for s in S:
        for x in range(MAX - 1, -1, -1):
            if dp[x] > 0:
                nx = (x | s) + 1
                if nx <= MAX:
                    dp[nx] = (dp[nx] + dp[x]) % MOD

    print(dp[MAX] % MOD)

if __name__ == "__main__":
    main()