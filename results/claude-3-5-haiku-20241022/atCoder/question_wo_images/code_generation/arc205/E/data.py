MOD = 998244353

n = int(input())
a = list(map(int, input().split()))

for k in range(n):
    product = 1
    a_k = a[k]
    for i in range(k + 1):
        if (a[i] | a_k) == a_k:
            product = (product * a[i]) % MOD
    print(product)