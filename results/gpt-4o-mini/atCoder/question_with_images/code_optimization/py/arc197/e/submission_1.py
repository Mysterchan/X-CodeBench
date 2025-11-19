def modinv(a, p):
    return pow(a, p - 2, p)

def C(a):
    if a < 2:
        return 0
    return a * (a - 1) // 2 % P

def C3(a):
    if a < 3:
        return 0
    return a * (a - 1) % P * (a - 2) % P * modinv(6, P) % P

def C4(a):
    if a < 4:
        return 0
    return a * (a - 1) % P * (a - 2) % P * (a - 3) % P * modinv(24, P) % P

def calc(N, H, W):
    if H < 2 * N or W < 2 * N:
        return 0

    h_limit = H - 2 * N + 1
    w_limit = W - 2 * N + 1

    if h_limit < 1 or w_limit < 1:
        return 0

    ans = (h_limit * (h_limit + 1) // 2 % P * C(w_limit) % P) % P
    ans = (ans * 2) % P  # Account for both orientations

    ans = (ans - (C3(h_limit) * C(w_limit) % P) + P) % P

    ans = (ans + C4(w_limit + 1) * C4(h_limit + 1) * 2 % P) % P

    return ans

P = 998244353
T = int(input())
results = []
for _ in range(T):
    N, H, W = map(int, input().split())
    results.append(calc(N, H, W))
print('\n'.join(map(str, results)))