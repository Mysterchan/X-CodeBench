MOD = 998244353

def modinv(n):
    return pow(n, MOD-2, MOD)

def modpow(n, m):
    res = 1
    while m > 0:
        if m & 1:
            res = res * n % MOD
        n = n * n % MOD
        m >>= 1
    return res

def modfac(n):
    res = 1
    for i in range(1, n+1):
        res = res * i % MOD
    return res

def modcomb(n, k):
    return modfac(n) * modinv(modfac(k) * modfac(n-k) % MOD) % MOD

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solve():
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i):
            if is_prime(i-j+1):
                dp[i] = (dp[i] + dp[j] * modpow(i-j, j*(i-j)) % MOD * modcomb(i, j) % MOD) % MOD
        dp[i] = (modpow(i, i*(i-1)//2) - dp[i]) % MOD
    print(dp[n])

if __name__ == "__main__":
    solve()