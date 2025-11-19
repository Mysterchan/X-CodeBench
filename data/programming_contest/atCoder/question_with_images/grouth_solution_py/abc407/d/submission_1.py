h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

n = h * w
dp = [False] * (1 << n)
dp[0] = True
res = 0
for s in range(1 << n):
    if dp[s]:
        cres = 0
        for x in range(h):
            for y in range(w):
                d = x * w + y
                if not (s >> d) & 1:
                    cres ^= a[x][y]
        if res < cres:
            res = cres

        for x in range(h):
            for y in range(w):
                d = x * w + y
                if not ((s >> d) & 1):
                    if x + 1 < h and not (s >> (d + w) & 1):
                        dp[s | 1 << d | 1 << (d + w)] = True
                    if y + 1 < w and not (s >> (d + 1) & 1):
                        dp[s | 1 << d | 1 << (d + 1)] = True

print(res)