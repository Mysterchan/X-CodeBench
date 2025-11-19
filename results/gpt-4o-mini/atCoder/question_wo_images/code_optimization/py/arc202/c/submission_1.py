import sys
from math import gcd

MOD = 998244353

def lcm(a, b):
    return (a * (b // gcd(a, b))) % MOD

input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:N + 1]))

R = [(10**a - 1) // 9 for a in A]  # Precompute R_a_i values
results = []
current_lcm = R[0]

results.append(current_lcm % MOD)

for i in range(1, N):
    current_lcm = lcm(current_lcm, R[i])
    results.append(current_lcm % MOD)

sys.stdout.write('\n'.join(map(str, results)) + '\n')