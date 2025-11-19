def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x // gcd(x, y) * y

MOD = 998244353

def R(n):
    # R_n is 'int' of n consecutive '1's which is 10^n - 1 // (10 - 1)
    return (10**n - 1) // 9

import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

current_lcm = 1
results = []

for k in range(N):
    current_lcm = lcm(current_lcm, R(A[k])) % MOD
    results.append(current_lcm)

print('\n'.join(map(str, results)))