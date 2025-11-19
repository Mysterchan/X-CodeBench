N, X, Y = map(int, input().split())
M = 998244353

# Precompute factorials and inverse factorials up to N
F = [1] * (N + 1)
for i in range(1, N + 1):
    F[i] = F[i-1] * i % M

G = [1] * (N + 1)
G[N] = pow(F[N], -1, M)
for i in range(N - 1, -1, -1):
    G[i] = G[i + 1] * (i + 1) % M

def comb(a, b):
    if b < 0 or b > a:
        return 0
    return F[a] * G[b] % M * G[a - b] % M

C = [0, 0, 0]
for _ in range(N):
    a, b = map(int, input().split())
    b %= 2
    
    if Y * (X + 1) % 2:
        if a - b >= 1:
            C[0] += 1
        elif b:
            C[1] += 1
        else:
            C[2] += 1
    elif X * (Y + 1) % 2:
        if a + b < 1:
            C[2] += 1
        elif (a < 2) * b:
            C[1] += 1
        else:
            C[0] += 1
    else:
        C[2 - bool([a % 2 - b, b][X * Y % 2])] += 1

# Build Q array
Q = [0] * (C[1] * 2 + 2)
for i in range(C[1] * 2 + 1):
    if i % 2 == 0:
        Q[i + 1] = Q[i] + comb(C[1], i // 2)
    else:
        Q[i + 1] = Q[i]

# Compute result
result = 0
threshold = C[1] + C[0] * (X * (Y + 1) % 2) + 1
for i in range(C[0] + 1):
    idx = min(C[1] * 2 + 1, max(0, threshold - i))
    result = (result + comb(C[0], i) * (Q[-1] - Q[idx])) % M

result = result * pow(2, C[2], M) % M
print(result)