MOD = 998244353

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = list(map(int, input().split()))

    MAX = 1 << N
    
    # Use dictionary to store only reachable states
    dp = {0: 1}
    
    # Process in order of increasing x values
    for x in range(MAX):
        if x not in dp:
            continue
        
        count = dp[x]
        
        for s in S:
            nx = (x | s) + 1
            if nx <= MAX:
                if nx not in dp:
                    dp[nx] = count
                else:
                    dp[nx] = (dp[nx] + count) % MOD

    print(dp.get(MAX, 0))

if __name__ == "__main__":
    main()