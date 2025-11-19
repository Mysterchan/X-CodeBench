import sys
input = sys.stdin.readline

mod = 998244353

n = int(input())
Y = list(map(int, input().split()))

two = [1] * (n + 1)
for i in range(1, n + 1):
    two[i] = (two[i - 1] * 2) % mod

def calc(p):
    r = 0
    prefix_sum = [0] * (n + 1)
    for y in p:
        prefix_sum[y] += 1
    for i in range(1, n + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    for i in range(n):
        left = p[i]
        r += (prefix_sum[n] - prefix_sum[left]) * two[p[i] - 1] % mod * (n - 1) % mod
        r %= mod
    return r

total = (two[n] - 1) * (n - 1) % mod

# Adjust the contribution of every individual prefix
total += calc(Y)
total += calc(Y[::-1])
total += calc([n - y for y in Y])
total += calc([n - y for y in Y][::-1])

# Subtract the over counted 4 * contributions from each element,
# since each element appears in 4 configurations
for i in range(1, n):
    total -= 4 * two[i] * (n - 1) % mod
    total %= mod

print(total)