N, M = map(int, input().split())
S = input()
mod = 998244353

# Precompute next occurrence of each character in S for each position
# next_pos[i][c] = next position of character c after index i-1 in S (1-based indexing)
next_pos = [[N + 1] * 26 for _ in range(N + 2)]
for i in range(N - 1, -1, -1):
    for c in range(26):
        next_pos[i + 1][c] = next_pos[i + 2][c]
    next_pos[i + 1][ord(S[i]) - ord('a')] = i + 1

# dp[i][k]: number of strings of length i with LCS length exactly k
# We'll use dp arrays for LCS length counts
# We use a DP over length and LCS length, counting how many strings have LCS length exactly k
# The total number of strings is 26^M

# To compute dp, we use a standard approach:
# Let f[i][l] = number of strings of length i whose LCS with S is at least l
# Then dp[i][k] = f[i][k] - f[i][k+1]

# We compute f[i][l] using DP:
# f[0][0] = 1, f[0][l>0] = 0
# For each position i in [0..M-1], for each l in [0..N], we consider adding a character c:
# If l < N and next_pos[l+1][c] <= N, then we can increase LCS length by 1
# So f[i+1][l'] += f[i][l] * (number of characters c that lead to l')
# We can precompute transitions for each l

# Precompute transitions:
trans = [ [0]*(N+2) for _ in range(N+1) ]  # trans[l][l'] = number of chars c that move from l to l'
for l in range(N+1):
    count = [0]*(N+2)
    for c in range(26):
        np = next_pos[l+1][c]
        if np <= N:
            count[np] += 1
        else:
            count[l] += 1
    for l2 in range(N+2):
        trans[l][l2] = count[l2]

f = [0]*(N+1)
f[0] = 1

for _ in range(M):
    nf = [0]*(N+1)
    for l in range(N+1):
        val = f[l]
        if val == 0:
            continue
        for l2 in range(N+1):
            c = trans[l][l2]
            if c:
                nf[l2] = (nf[l2] + val * c) % mod
    f = nf

ans = [0]*(N+1)
for k in range(N):
    ans[k] = (f[k] - f[k+1]) % mod
ans[N] = f[N] % mod

print(*ans)