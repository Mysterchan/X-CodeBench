from collections import defaultdict

INF = 10**10
def solve(h, w, S):
    memo = [dict() for i in range(1<<w)]
    def generate(base, bitmask, d):
        if bitmask in memo[base]:
            return
        memo[base][bitmask] = d
        for j in range(w):
            if (bitmask >> j) & 1:
                generate(base, bitmask-(1<<j), d+1)

    B = [0]*h
    for i in range(h):
        bitmask = 0
        for j in range(w):
            if S[i][j] == "#":
                bitmask |= 1<<j
        B[i] = bitmask
        generate(bitmask, bitmask, 0)

    def satisfied(lines):

        for j in range(w-1):
            passed = False
            for i in range(2):
                for dj in [0, 1]:
                    nj = j + dj
                    if (lines[i] >> nj) & 1 == 0:
                        passed = True
                        break
            if not passed:

                return False
        return True

    dp = [[INF]*(1<<w) for i in range(h)]
    for bitmask, d in memo[B[0]].items():
        dp[0][bitmask] = d
    for i in range(1, h):
        for bitmask, d in memo[B[i]].items():
            for prev_bitmask, _ in memo[B[i-1]].items():
                if satisfied([bitmask, prev_bitmask]):
                    dp[i][bitmask] = min(dp[i][bitmask], dp[i-1][prev_bitmask] + d)
    return min(dp[-1])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        S = [input() for i in range(h)]
        print(solve(h, w, S))