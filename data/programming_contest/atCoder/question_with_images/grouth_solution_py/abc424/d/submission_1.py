def solve(h, w, S):
    INF = 10**9
    B = []
    for i in range(h):
        bit = 0
        for j in range(w):
            if S[i][j] == '#':
                bit |= 1 << j
        B.append(bit)

    ok = [[False]*(1<<w) for _ in range(1<<w)]
    mask = (1 << (w - 1)) - 1
    for a in range(1<<w):
        for b in range(1<<w):

            ok[a][b] = not (((a & (a >> 1)) & (b & (b >> 1))) & mask)

    dp_prev = [INF]*(1<<w)
    for bit in range(1<<w):
        dp_prev[bit] = (B[0] ^ bit).bit_count()

    for i in range(1, h):
        dp_cur = [INF]*(1<<w)
        for bit in range(1<<w):
            cost = (B[i] ^ bit).bit_count()
            for prev in range(1<<w):
                if ok[bit][prev]:
                    dp_cur[bit] = min(dp_cur[bit], dp_prev[prev] + cost)
        dp_prev = dp_cur

    return min(dp_prev)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        S = [input() for i in range(h)]
        print(solve(h, w, S))