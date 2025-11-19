MOD = 998244353
import sys

def precompute_factorials(max_n, mod=MOD):
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
    for i in range(max_n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod
    return fact, inv_fact

maxN = 200000
fact, inv_fact = precompute_factorials(maxN, MOD)

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n

        a1 = a[0]
        if a1 < 2:
            results.append("0")
            continue

        rem = a1 - 2
        total_columns = n - 2
        if rem < 0:
            comb = 0
        else:
            if rem > total_columns:
                comb = 0
            else:
                comb = nCr(total_columns, rem)

        for i in range(2, n + 1):
            if rem <= 0:
                break
            take = min(rem, i - 1)
            comb = comb * take % MOD
            rem -= take

        if rem != 0:
            results.append("0")
        else:
            results.append(str(comb))

    print("\n".join(results))

if __name__ == "__main__":
    main()
