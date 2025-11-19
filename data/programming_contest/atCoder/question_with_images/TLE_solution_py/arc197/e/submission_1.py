def C(a):
    return a * (a - 1) // 2 % P
def C3(a):
    return a * (a - 1) % P * (a - 2) % P * 166374059 % P
def C4(a):
    return a * (a - 1) % P * (a - 2) % P * (a - 3) % P * 291154603 % P

def calc(N, H, W):
    if H < 2 * N or W < 2 * N:
        return 0
    def calc_h(h):
        if h < N or H - h < N:
            return 0
        return (h - N + 1) ** 2 % P * (C(W - 2 * N + 2) ** 2 % P) % P * (2 * (H - h - N + 1) - 1) % P
    def calc_w(w):
        if w < N or W - w < N:
            return 0
        return (w - N + 1) ** 2 % P * (C(H - 2 * N + 2) ** 2 % P) % P * (2 * (W - w - N + 1) - 1) % P
    def sub_calc_h(h):
        if h < N or H - h < N:
            return 0
        return (h - N + 1) ** 2 % P * (2 * (H - h - N + 1) - 1) % P
    def sub_calc_w(w):
        if w < N or W - w < N:
            return 0
        return (w - N + 1) ** 2 % P * (2 * (W - w - N + 1) - 1) % P
    ans = 0
    for h in range(N, H - N + 1):
        ans = (ans + calc_h(h)) % P
    for w in range(N, W - N + 1):
        ans = (ans + calc_w(w)) % P
    t1 = 0
    for h in range(N, H - N + 1):
        t1 = (t1 + sub_calc_h(h)) % P
    t2 = 0
    for w in range(N, W - N + 1):
        t2 = (t2 + sub_calc_w(w)) % P
    ans = (ans - t1 * t2) % P
    ans = (ans + C4(W - 2 * N + 3) * C4(H - 2 * N + 3) * 2) % P
    return ans

P = 998244353
T = int(input())
for _ in range(T):
    N, H, W = map(int, input().split())
    print(calc(N, H, W))