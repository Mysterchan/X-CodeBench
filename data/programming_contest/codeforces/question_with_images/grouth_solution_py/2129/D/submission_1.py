from functools import cache
from sys import stdin, setrecursionlimit
input = lambda: stdin.readline().rstrip()
setrecursionlimit(10 ** 5)
mod = 998244353

MAXN = 100
C = [[0] * (MAXN + 1) for _ in range(MAXN + 1)]
for i in range(MAXN + 1):
    C[i][0] = 1
    for j in range(1, i + 1):
        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod


def solve():
    n = int(input())
    s = list(map(int, input().split()))
    if max(s) > (n.bit_length() - 1) * 2:
        return 0
    res = 0
    for x in s:
        if x > 0:
            res += x
    if res > n - 1:
        return 0

    @cache
    def dfs(l: int, r: int, pl: int, pr: int) -> int:
        if l > r:
            return int(pl <= 1 and pr <= 1)

        ans = 0

        for k in range(l, r + 1):
            p0 = int(l > 0 and (r == n - 1 or (k - l) <= (r - k)))
            p1 = int(r < n - 1 and (l == 0 or (k - l) > (r - k)))

            if (pl == 1 and p0) or (pr == 1 and p1):
                continue

            left_pl = pl - p0
            right_pr = pr - p1

            res = 0
            if s[k] == -1:
                left = dfs(l, k - 1, left_pl, 0)
                right = dfs(k + 1, r, 0, right_pr)
                res = (res + left * right) % mod
            else:
                sk = s[k]
                for o in range(sk + 1):
                    left = dfs(l, k - 1, left_pl, o + 1)
                    right = dfs(k + 1, r, sk - o + 1, right_pr)
                    res = (res + left * right) % mod

            ans = (ans + C[r - l][k - l] * res) % mod

        return ans

    return dfs(0, n - 1, 1, 1)


for _ in range(int(input())):
    print(solve())
