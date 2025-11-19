def main():
    mod = 998244353
    n = int(input())
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    ans = 0
    for i in range(1, n + 1):
        x = str(i)
        y = len(x)
        z = (fact[n - 1] * (n)) % mod
        for j in range(y):
            z = (z * 10) % mod
        ans = (ans + (z * int(x)) % mod) % mod

    print(ans)

if __name__ == "__main__":
    main()