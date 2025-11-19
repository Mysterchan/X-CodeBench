import sys
input = sys.stdin.readline

def optimized_graph_count(n: int, p: int) -> list[int]:
    edge = n * (n - 1) // 2
    mid = n // 2 + 1
    
    # Initialize combinatorial coefficients
    comb = [[0] * (edge + 1) for _ in range(mid + 1)]
    for i in range(mid + 1):
        comb[i][0] = 1  # C(i, 0) = 1
        for j in range(1, i + 1):
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % p
    
    # C array to hold counts of corresponding graphs
    c = [[[0] * (edge + 1) for _ in range(mid)] for _ in range(mid)]
    
    for px in range(mid):
        c[px][0][0] = 1
        for dx in range(n // 2):
            for pe in range(edge + 1):
                for de in range(1, edge + 1 - pe):
                    c[px][dx + 1][pe + de] += c[px][dx][pe] * comb[px][de] % p
                    c[px][dx + 1][pe + de] %= p

    # Calculate s_count using the computed c
    sc = [[[0] * (edge + 1) for _ in range(mid)] for _ in range(mid)]
    for px in range(mid):
        for dx in range(mid):
            for de in range(edge + 1):
                res = 0
                for pe in range(dx, de + 1):
                    res += c[px][dx][pe] * comb[dx * (dx - 1) // 2][de - pe] % p
                    res %= p
                sc[px][dx][de] = res

    dp = [0] * (2 * (edge + 1) * mid * mid * mid)
    dp[mid * mid + 1] = 1
    
    # Calculate the graphs count for valid (i, j) combinations
    for e in range(edge + 1):
        for i in range(min(mid, e + 2)):
            for j in range(min(mid, e - i + 2)):
                for px in range(1, mid):
                    if dp[mid * mid * mid + e * (mid * mid * mid) + i * (mid * mid) + j * (mid) + px]:
                        q = dp[mid * mid * mid + e * (mid * mid * mid) + i * (mid * mid) + j * (mid) + px] % p
                        for dx in range(1, min(n + 1 - i - j, mid - i)):
                            for de in range(dx, edge + 1 - e):
                                dp[(e + de) * (mid * mid * mid) + (i + dx) * (mid * mid) + j * (mid) + dx] += comb[n - i - j][dx] * q % p * sc[px][dx][de] % p
                                dp[(e + de) * (mid * mid * mid) + (i + dx) * (mid * mid) + j * (mid) + dx] %= p
                if dp[e * (mid * mid * mid) + i * (mid * mid) + j * (mid) + px]:
                    q = dp[e * (mid * mid * mid) + i * (mid * mid) + j * (mid) + px] % p
                    for dx in range(1, min(n + 1 - i - j, mid - j)):
                        for de in range(dx, edge + 1 - e):
                            dp[mid * mid * mid + (e + de) * (mid * mid) + i * (mid * mid) + (j + dx) * (mid) + dx] += comb[n - i - j][dx] * q % p * sc[px][dx][de] % p
                            dp[mid * mid * mid + (e + de) * (mid * mid) + i * (mid * mid) + (j + dx) * (mid) + dx] %= p

    # Collect results for output
    tans = []
    for m in range(n - 1, edge + 1):
        ans = 0
        for px in range(mid):
            off = m * (mid * mid * mid) + (mid - 1) * (mid * mid) + (mid - 1) * mid
            ans = (ans + dp[off + px] + dp[mid * mid * mid + off + px]) % p
        tans.append(ans)

    return tans

# Read input
n, p = map(int, input().split())
result = optimized_graph_count(n, p)
print(*result)