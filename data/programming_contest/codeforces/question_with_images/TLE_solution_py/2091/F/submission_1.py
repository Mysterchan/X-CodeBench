from sys import stdout, setrecursionlimit
from math import ceil, floor
def query(a: list): pass
def answer(x: int): pass

MOD = 998244353
def solve():
    n, m, d = map(int, input().split(" "))
    grid = []
    for _ in range(n): grid.append(list(input()))
    dp1 = [[0] * m for _ in range(n)]
    dp2 = [[0] * m for _ in range(n)]
    dp = [[0] * m for _ in range(n)]

    prfx1 = [[0] * m for _ in range(n)]
    prfx2 = [[0] * m for _ in range(n)]
    def getPrfx(row: int, l: int, r: int, prfx: list[int]):
        if row >= n or l > r: return 0
        left = 0 if l <= 0 else prfx[row][l-1]
        right = prfx[row][min(r, m-1)]
        return (right - left) % MOD


    for j in range(m):
        dp1[n-1][j] = 1 if grid[n-1][j] == "X" else 0

    res = 0
    for i in range(n-1, -1, -1):
        for j in range(m):

            if grid[i][j] == "X": dp1[i][j] = (dp1[i][j] + getPrfx(i+1, j - d + 1, j + d - 1, prfx2)) % MOD
            if j != 0: prfx1[i][j] = prfx1[i][j-1]
            prfx1[i][j] = (prfx1[i][j] + dp1[i][j]) % MOD

        for j in range(m):
            if grid[i][j] == "X":
                dp2[i][j] = (getPrfx(i, j - d, j + d, prfx1) + getPrfx(i+1, j - d + 1, j + d - 1, prfx2) - dp1[i][j]) % MOD
                if i == n-1: dp2[i][j] += 1

            if j != 0: prfx2[i][j] = prfx2[i][j-1]
            prfx2[i][j] += dp2[i][j]



    res = sum(dp2[0])

    print(res % MOD)


for _ in range(int(input())): solve()
