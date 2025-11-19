MOD = 998244353

N = int(input())
if N == 1:
    print(1)
else:
    result = pow(N - 1, N - 1, MOD)
    print(result)