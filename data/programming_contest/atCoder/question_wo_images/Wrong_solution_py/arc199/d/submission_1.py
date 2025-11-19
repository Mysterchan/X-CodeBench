MOD = 998244353

def main():
    import sys
    data = sys.stdin.read().split()
    H = int(data[0])
    W = int(data[1])

    inv4 = pow(4, MOD - 2, MOD)

    T1 = H % MOD
    T1 = (T1 * W) % MOD
    T1 = T1 * pow(W + 1, H, MOD) % MOD
    T1 = T1 * pow(H + 1, W, MOD) % MOD

    base1 = pow(W + 1, H - 1, MOD)
    base2 = pow(H + 1, W - 1, MOD)
    T2 = base1 * base2 % MOD
    T2 = T2 * (H % MOD) % MOD
    T2 = T2 * ((H + 1) % MOD) % MOD
    T2 = T2 * (W % MOD) % MOD
    T2 = T2 * ((W + 1) % MOD) % MOD
    T2 = T2 * inv4 % MOD

    ans = (T1 - T2) % MOD
    if ans < 0:
        ans += MOD
    print(ans)

if __name__ == "__main__":
    main()