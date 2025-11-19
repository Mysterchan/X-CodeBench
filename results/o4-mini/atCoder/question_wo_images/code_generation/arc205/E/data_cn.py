import sys
input = sys.stdin.readline

MOD = 998244353
MAX_MASK = 1 << 20

N = int(input())
A = list(map(int, input().split()))

# freq[mask]: product of all A_i with value == mask, modulo MOD
freq = [1] * MAX_MASK
count = [0] * MAX_MASK  # count of elements with value == mask

for x in A:
    freq[x] = (freq[x] * x) % MOD
    count[x] += 1

# superset product transform (zeta transform over supersets)
# After this, freq[mask] = product of all A_i with value superset of mask
for bit in range(20):
    for mask in range(MAX_MASK):
        if (mask & (1 << bit)) == 0:
            freq[mask] = (freq[mask] * freq[mask | (1 << bit)]) % MOD

# For each k, output freq[A_k]
for x in A:
    print(freq[x] % MOD)