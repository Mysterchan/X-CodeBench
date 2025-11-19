MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

for k in range(N):
    result = 1
    for i in range(k + 1):
        if (A[i] | A[k]) == A[k]:
            result = (result * A[i]) % MOD
    print(result)