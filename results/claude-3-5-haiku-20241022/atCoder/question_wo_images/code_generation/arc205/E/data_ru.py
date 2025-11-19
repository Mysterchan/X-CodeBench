MOD = 998244353

n = int(input())
a = list(map(int, input().split()))

for k in range(n):
    ak = a[k]
    product = 1
    for i in range(k + 1):
        if (a[i] | ak) == ak:
            product = (product * a[i]) % MOD
    print(product)