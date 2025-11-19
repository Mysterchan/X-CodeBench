MOD = 998244353

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = list(map(int, input().split()))

    MAX = 1 << N
    dp = [0] * (MAX + 1)
    dp[0] = 1

    for x in range(MAX):
        if dp[x] == 0:
            continue
        for s in S:
            nx = (x | s) + 1
            if nx <= MAX:
                dp[nx] = (dp[nx] + dp[x]) % MOD

    print(dp[MAX] % MOD)

if __name__ == "__main__":
    main()