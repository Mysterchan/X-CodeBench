import sys

input = sys.stdin.read
data = input().split()

MOD = 998244353
N = int(data[0])
Y = list(map(int, data[1:]))

pos = [0] * (N + 1)
for i in range(1, N + 1):
    pos[Y[i - 1]] = i

sum_left_x = [0] * (N + 2)
for l in range(1, N + 1):
    sum_left_x[l] = (sum_left_x[l - 1] + l) % MOD

sum_right_x = [0] * (N + 2)
sum_right_x[N + 1] = 0
for r in range(N, 0, -1):
    sum_right_x[r] = (sum_right_x[r + 1] + r) % MOD

total_x = 0
for p in range(1, N + 1):
    left_count = pos[p] - 1
    right_count = N - pos[p]
    contrib_x = (left_count * sum_right_x[pos[p] + 1] + right_count * sum_left_x[pos[p] - 1]) % MOD
    total_x = (total_x + contrib_x) % MOD

sum_left_y = [0] * (N + 2)
for l in range(1, N + 1):
    sum_left_y[l] = (sum_left_y[l - 1] + pos[l]) % MOD

sum_right_y = [0] * (N + 2)
sum_right_y[N + 1] = 0
for r in range(N, 0, -1):
    sum_right_y[r] = (sum_right_y[r + 1] + pos[r]) % MOD

total_y = 0
for q in range(1, N + 1):
    left_count = q - 1
    right_count = N - q
    contrib_y = (left_count * sum_right_y[q + 1] + right_count * sum_left_y[q - 1]) % MOD
    total_y = (total_y + contrib_y) % MOD

total = (total_x + total_y) % MOD
print(total)