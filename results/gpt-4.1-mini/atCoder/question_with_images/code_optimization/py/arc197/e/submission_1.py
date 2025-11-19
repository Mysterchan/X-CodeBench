P = 998244353

inv2 = 499122177  # modular inverse of 2 mod P
inv3 = 332748118  # modular inverse of 3 mod P
inv6 = 166374059  # modular inverse of 6 mod P
inv24 = 291154603 # modular inverse of 24 mod P

def mod_add(a, b):
    return (a + b) % P

def mod_sub(a, b):
    return (a - b) % P

def mod_mul(a, b):
    return (a * b) % P

def mod_pow(a, b):
    res = 1
    base = a % P
    e = b
    while e > 0:
        if e & 1:
            res = (res * base) % P
        base = (base * base) % P
        e >>= 1
    return res

def sum_k(k):
    # sum of first k natural numbers: k*(k+1)//2 mod P
    return mod_mul(k, k + 1) * inv2 % P

def sum_k2(k):
    # sum of squares of first k natural numbers: k*(k+1)*(2k+1)//6 mod P
    return mod_mul(mod_mul(k, k + 1), 2 * k + 1) * inv6 % P

def sum_k3(k):
    # sum of cubes of first k natural numbers: (k*(k+1)//2)^2 mod P
    s = mod_mul(k, k + 1) * inv2 % P
    return mod_mul(s, s)

def C(a):
    # C(a) = a*(a-1)//2 mod P
    return mod_mul(a, a - 1) * inv2 % P

def C4(a):
    # a*(a-1)*(a-2)*(a-3)/24 mod P
    return mod_mul(mod_mul(mod_mul(a, a - 1), a - 2), a - 3) * inv24 % P

def sum_sq(l, r):
    # sum of i^2 for i in [l, r]
    if r < l:
        return 0
    return (sum_k2(r) - sum_k2(l - 1)) % P

def sum_i(l, r):
    # sum of i for i in [l, r]
    if r < l:
        return 0
    return (sum_k(r) - sum_k(l - 1)) % P

def sum_const(l, r, c):
    # sum of constant c for i in [l, r]
    if r < l:
        return 0
    return mod_mul(c, (r - l + 1) % P)

def calc(N, H, W):
    if H < 2 * N or W < 2 * N:
        return 0

    # Precompute some constants
    A = W - 2 * N + 2
    B = H - 2 * N + 2

    if A < 1 or B < 1:
        return 0

    # Precompute C(A) and C(B)
    CA = C(A)
    CB = C(B)

    # sum over h in [N, H-N]
    # calc_h(h) = (h - N + 1)^2 * (C(W - 2N + 2)^2) * (2*(H - h - N + 1) - 1)
    # Let x = h - N + 1, h in [N, H-N] => x in [1, H - 2N + 1] = [1, B - 1]
    # Let y = H - h - N + 1 = (H - N + 1) - h = (H - N + 1) - (x + N - 1) = (H - 2N + 2) - x = B - x

    # So calc_h(h) = x^2 * (CA^2) * (2*(B - x) - 1) = x^2 * (CA^2) * (2B - 2x - 1)
    # = (CA^2) * (x^2 * (2B - 1) - 2 x^3)

    CA2 = mod_mul(CA, CA)
    B_mod = B % P

    # sum over x=1 to B-1 of x^2 * (2B - 1) - 2 x^3
    # = (2B - 1) * sum x^2 - 2 * sum x^3

    if B - 1 < 1:
        sum_calc_h = 0
    else:
        sum_x2 = sum_k2(B - 1)
        sum_x3 = 0
        # sum of cubes: sum_k3(B-1)
        sum_x3 = sum_k3(B - 1)
        part1 = mod_mul((2 * B_mod - 1) % P, sum_x2)
        part2 = mod_mul(2, sum_x3)
        sum_calc_h = mod_mul(CA2, mod_sub(part1, part2))

    # sum over w in [N, W-N]
    # calc_w(w) = (w - N + 1)^2 * (C(H - 2N + 2)^2) * (2*(W - w - N + 1) - 1)
    # similarly, let x = w - N + 1 in [1, A - 1]
    # y = W - w - N + 1 = (W - 2N + 2) - x = A - x

    CB2 = mod_mul(CB, CB)
    A_mod = A % P

    if A - 1 < 1:
        sum_calc_w = 0
    else:
        sum_x2_w = sum_k2(A - 1)
        sum_x3_w = sum_k3(A - 1)
        part1_w = mod_mul((2 * A_mod - 1) % P, sum_x2_w)
        part2_w = mod_mul(2, sum_x3_w)
        sum_calc_w = mod_mul(CB2, mod_sub(part1_w, part2_w))

    ans = mod_add(sum_calc_h, sum_calc_w)

    # t1 = sum over h in [N, H-N] of sub_calc_h(h) = (h - N + 1)^2 * (2*(H - h - N + 1) - 1)
    # = x^2 * (2*(B - x) - 1) = x^2 * (2B - 2x - 1) = x^2*(2B -1) - 2 x^3
    if B - 1 < 1:
        t1 = 0
    else:
        sum_x2 = sum_k2(B - 1)
        sum_x3 = sum_k3(B - 1)
        part1 = mod_mul((2 * B_mod - 1) % P, sum_x2)
        part2 = mod_mul(2, sum_x3)
        t1 = mod_sub(part1, part2)

    # t2 = sum over w in [N, W-N] of sub_calc_w(w) = (w - N + 1)^2 * (2*(W - w - N + 1) - 1)
    # similarly
    if A - 1 < 1:
        t2 = 0
    else:
        sum_x2 = sum_k2(A - 1)
        sum_x3 = sum_k3(A - 1)
        part1 = mod_mul((2 * A_mod - 1) % P, sum_x2)
        part2 = mod_mul(2, sum_x3)
        t2 = mod_sub(part1, part2)

    ans = mod_sub(ans, mod_mul(t1, t2))

    # last term: C4(W - 2N + 3) * C4(H - 2N + 3) * 2
    # Let a = W - 2N + 3, b = H - 2N + 3
    a = W - 2 * N + 3
    b = H - 2 * N + 3
    if a < 4 or b < 4:
        last_term = 0
    else:
        last_term = mod_mul(C4(a), C4(b))
        last_term = mod_mul(last_term, 2)

    ans = mod_add(ans, last_term)

    return ans % P

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, H, W = map(int, input().split())
    print(calc(N, H, W))