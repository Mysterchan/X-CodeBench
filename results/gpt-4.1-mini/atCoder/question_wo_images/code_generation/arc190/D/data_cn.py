import sys
input = sys.stdin.readline

def matmul(A, B, p):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for j in range(n):
            s = 0
            for k in range(n):
                s += Ai[k]*B[k][j]
            C[i][j] = s % p
    return C

def matadd(A, B, p):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Bi = B[i]
        for j in range(n):
            C[i][j] = (Ai[j] + Bi[j]) % p
    return C

def matpow(A, p, mod):
    n = len(A)
    R = [[0]*n for _ in range(n)]
    for i in range(n):
        R[i][i] = 1
    base = A
    e = p
    while e > 0:
        if e & 1:
            R = matmul(R, base, mod)
        base = matmul(base, base, mod)
        e >>= 1
    return R

N, p = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# Count zeros and record their positions
zero_positions = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            zero_positions.append((i,j))
K = len(zero_positions)

# If no zeros, B = A only, sum = B^p
if K == 0:
    Bp = matpow(A, p, p)
    for row in Bp:
        print(*row)
    exit()

# Precompute sum_{x=1}^{p-1} x^m mod p for m=0..p-1
# Using Fermat's little theorem and properties of finite fields:
# sum_{x=1}^{p-1} x^m mod p = 0 if m mod (p-1) != 0, else p-1
# Because p is prime, and the multiplicative group mod p is cyclic of order p-1.
# So sum_{x=1}^{p-1} x^m = 0 if m%(p-1)!=0 else p-1 (mod p)
# Note: p-1 mod p = p-1

def sum_powers(m):
    if m % (p-1) == 0:
        return (p-1) % p
    else:
        return 0

# We want to compute:
# sum_{all B} B^p mod p
# where B differs from A only at zero positions, replaced by values in [1,p-1]

# Key insight:
# Over field of char p, (X+Y)^p = X^p + Y^p
# So B^p = (A + C)^p = A^p + C^p, where C is the matrix of zero replacements (nonzero only at zero positions)
# Because A and C have disjoint supports, and char p, cross terms vanish.

# So sum_B B^p = sum_B (A^p + C^p) = (p-1)^K * A^p + sum_B C^p

# Now sum_B C^p:
# C has zeros except at zero_positions, where entries are in [1,p-1]
# C^p = C (since for each entry c, c^p = c mod p)
# So C^p = C

# sum_B C^p = sum_B C = matrix where each zero position (i,j) is sum over all assignments of c_{i,j} in [1,p-1],
# and other zero positions vary independently.

# Number of assignments: (p-1)^K
# For sum over all B, sum of C at position (i,j):
# - If (i,j) not zero position: always 0
# - If (i,j) zero position:
#   sum over all assignments = sum_{c=1}^{p-1} c * (p-1)^{K-1} (since other zero positions vary freely)
# sum_{c=1}^{p-1} c = (p-1)*p/2 mod p
# But p is prime, so p mod p=0, so sum_{c=1}^{p-1} c mod p = 0
# So sum_{c=1}^{p-1} c mod p = 0

# So sum_B C = zero matrix mod p

# Therefore:
# sum_B B^p = (p-1)^K * A^p mod p

# Compute A^p mod p
Ap = matpow(A, p, p)

# Compute (p-1)^K mod p
# Since p is prime, (p-1) mod p = p-1
# (p-1)^K mod p = (-1)^K mod p
# If K even: 1
# If K odd: p-1

if K % 2 == 0:
    coef = 1
else:
    coef = p - 1

# Multiply Ap by coef mod p
for i in range(N):
    for j in range(N):
        Ap[i][j] = (Ap[i][j] * coef) % p

for row in Ap:
    print(*row)