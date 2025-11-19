import sys
input = sys.stdin.readline

MOD = 998244353
N = int(input())
A = list(map(int, input().split()))

dp = [1] * (1 << 20)
results = []

for k in range(N):
    x = A[k]
    product = 1
    
    # Traverse all numbers in the sequence so far
    for i in range(k + 1):
        if A[i] | x == x:
            product = (product * A[i]) % MOD
            
    results.append(product)

print('\n'.join(map(str, results)))