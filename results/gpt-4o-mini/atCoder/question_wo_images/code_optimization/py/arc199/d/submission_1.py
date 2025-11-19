mod = 998244353

h, w = map(int, input().split())
if h < w:
    h, w = w, h

total_matrices = pow(2, h + w - 2, mod)
sum_value = 0

# Each cell (i, j) will be set to 1 in total_matrices configurations.
for r in range(1, h + 1):
    for c in range(1, w + 1):
        # Count the contribution of setting each (r, c) position
        # The number of configurations where A[i][j] is 1 will be:
        # (2^(r-1) * 2^(h-r)) * (2^(c-1) * 2^(w-c)) = 2^(r + c - 2 + (h - r) + (w - c))
        # which simplifies to 2^(h + w - 2)
        sum_value += total_matrices

sum_value %= mod
print(sum_value)