import sys

MOD = 998244353

MAX_K = 400005
fact = [1] * (MAX_K + 1)
inv_fact = [1] * (MAX_K + 1)
for i in range(1, MAX_K + 1):
    fact[i] = (fact[i - 1] * i) % MOD

inv_fact[MAX_K] = pow(fact[MAX_K], MOD - 2, MOD)
for i in range(MAX_K - 1, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

def nCr_mod(n, r):

    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    if r > n // 2:
        r = n - r

    if n < MAX_K:
        num = fact[n]
        den = (inv_fact[r] * inv_fact[n - r]) % MOD
        return (num * den) % MOD

    num = 1
    for i in range(r):
        num = (num * (n - i)) % MOD
    return (num * inv_fact[r]) % MOD

def solve():
    H, W, K = map(int, sys.stdin.readline().split())

    total_walls_base = 2 * H * W - H - W

    term_A = 0
    for j in range(H):
        n = total_walls_base - j * W
        if n < K:

            break
        term = (nCr_mod(H - 1, j) * nCr_mod(n, K)) % MOD
        if j % 2 == 1:
            term_A = (term_A - term + MOD) % MOD
        else:
            term_A = (term_A + term) % MOD

    term_B = 0
    for l in range(W):
        n = total_walls_base - l * H
        if n < K:
            break
        term = (nCr_mod(W - 1, l) * nCr_mod(n, K)) % MOD
        if l % 2 == 1:
            term_B = (term_B - term + MOD) % MOD
        else:
            term_B = (term_B + term) % MOD

    term_C = 0
    for j in range(H):
        base_n = total_walls_base - j * W
        term_j = nCr_mod(H - 1, j)
        if term_j == 0: continue

        for l in range(W):
            n = base_n - l * H
            if n < K:
                break

            term_l = nCr_mod(W - 1, l)
            if term_l == 0: continue

            comb_term = nCr_mod(n, K)
            full_term = (term_j * term_l * comb_term) % MOD

            if (j + l) % 2 == 1:
                term_C = (term_C - full_term + MOD) % MOD
            else:
                term_C = (term_C + full_term) % MOD

    ans = (term_A + term_B - term_C + MOD) % MOD
    print(ans)

def main():
    try:
        T = int(sys.stdin.readline())
        for _ in range(T):
            solve()
    except (IOError, IndexError):

        pass

if __name__ == "__main__":
    main()