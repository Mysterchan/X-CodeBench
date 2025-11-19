import sys
input = sys.stdin.readline

def matmul(A, B, p):
    n = len(A)
    m = len(B[0])
    l = len(B)
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for k in range(l):
            Aik = Ai[k]
            Bk = B[k]
            for j in range(m):
                C[i][j] = (C[i][j] + Aik * Bk[j]) % p
    return C

def matpow(A, e, p):
    n = len(A)
    R = [[0]*n for _ in range(n)]
    for i in range(n):
        R[i][i] = 1
    base = A
    while e > 0:
        if e & 1:
            R = matmul(R, base, p)
        base = matmul(base, base, p)
        e >>= 1
    return R

N, p = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# Count zeros and build matrix C where zeros replaced by 0, non-zeros remain
# We will use the formula:
# sum_{B} B^p = (p-1)^K * A^p + (p-1)^{K-1} * p * (A^{p-1} * Z)
# where Z is the matrix with 1 at zero positions and 0 elsewhere

K = 0
Z = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            K += 1
            Z[i][j] = 1

# Compute A^p mod p
Ap = matpow(A, p, p)

if K == 0:
    # No zeros, sum is just A^p
    for row in Ap:
        print(*row)
    sys.exit()

# Compute A^{p-1} mod p
Ap1 = matpow(A, p-1, p)

# Compute Ap1 * Z mod p
Ap1Z = matmul(Ap1, Z, p)

# Compute (p-1)^K mod p
# Since p is prime, (p-1) ≡ -1 mod p
# So (p-1)^K ≡ (-1)^K mod p
pow_p_1_K = pow(p-1, K, p)
pow_p_1_K_1 = pow(p-1, K-1, p) if K > 0 else 0

# sum = (p-1)^K * Ap + (p-1)^{K-1} * p * Ap1Z mod p
# But p * Ap1Z mod p = 0, so second term is zero mod p
# So sum mod p = (p-1)^K * Ap mod p

# However, the problem's sample outputs show non-zero results,
# so we must consider the sum over integers, then mod p.

# The sum over all B of B^p is:
# sum_B B^p = (p-1)^K * A^p + (p-1)^{K-1} * p * (A^{p-1} * Z)
# We compute this sum modulo p.

# Since p * (anything) mod p = 0, the second term vanishes mod p.
# So sum mod p = (p-1)^K * A^p mod p

# But (p-1) ≡ -1 mod p, so (p-1)^K ≡ (-1)^K mod p

sign = pow(p-1, K, p)  # same as (-1)^K mod p

# Compute final matrix
res = [[(sign * Ap[i][j]) % p for j in range(N)] for i in range(N)]

for row in res:
    print(*row)