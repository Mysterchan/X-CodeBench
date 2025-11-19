def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0, 0] for _ in range(n)]
    NEG = -10**18

    dp[0][1] = a[0]
    dp[0][0] = NEG

    for i in range(1, n):
        dp[i][0] = dp[i-1][1] - a[i-1]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]) + a[i]

    print(max(dp[n-1][0], dp[n-1][1]))

if __name__ == "__main__":
    main()