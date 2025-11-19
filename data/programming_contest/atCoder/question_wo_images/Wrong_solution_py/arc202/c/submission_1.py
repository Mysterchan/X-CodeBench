MOD = 998244353

def modinv(a, mod):
    return pow(a, mod - 2, mod)

def compute_R(n):
    return (pow(10, n, MOD * 9) - 1) // 9

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_mod(a, b):
    return (a * b // gcd(a, b)) % MOD

def solve(A):
    from math import gcd
    result = []
    current_lcm = 1
    for a in A:
        R = compute_R(a)
        current_lcm = (current_lcm * R // gcd(current_lcm, R)) % MOD
        result.append(current_lcm)
    return result

import sys
input = sys.stdin.read
data = list(map(int, input().split()))
N = data[0]
A = data[1:]

ans = solve(A)
for val in ans:
    print(val)