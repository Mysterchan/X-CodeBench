R = range
f = lambda: map(int, input().split())
N, X, Y = f()
M = 998244353
F = [1]
G = [1]

def mod_inv(a, m):
    return pow(a, m - 2, m)

while len(F) <= N:
    F.append(F[-1] * len(F) % M)
    G.append(mod_inv(F[-1], M))

C = [0] * 3

for _ in range(N):
    a, b = f()
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

Q = [0] + [F[C[1]] * mod_inv(F[i], M) * mod_inv(F[C[1] * 2 - i], M) % M * (1 - i % 2) for i in R(C[1] * 2 + 1)]
for i in R(1, C[1] * 2 + 1):
    Q[i] = (Q[i] + Q[i - 1]) % M

result = sum(F[C[0]] * mod_inv(F[i], M) * mod_inv(F[C[0] + C[1] * 2 - i], M) % M * (Q[-1] - Q[max(0, C[1] * 2 + C[0] * (X * (Y + 1) % 2) - i)]) for i in R(C[0] + 1)) % M
print(result * pow(2, C[2], M) % M)