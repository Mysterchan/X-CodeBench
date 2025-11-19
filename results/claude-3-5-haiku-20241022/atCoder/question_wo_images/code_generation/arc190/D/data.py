def matmul(A, B, p):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % p
    return C

def matpow(A, exp, p):
    n = len(A)
    if exp == 0:
        I = [[0] * n for _ in range(n)]
        for i in range(n):
            I[i][i] = 1
        return I
    if exp == 1:
        return [row[:] for row in A]
    
    half = matpow(A, exp // 2, p)
    result = matmul(half, half, p)
    if exp % 2 == 1:
        result = matmul(result, A, p)
    return result

N, p = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

zeros = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            zeros.append((i, j))

K = len(zeros)
result = [[0] * N for _ in range(N)]

if K == 0:
    result = matpow(A, p, p)
else:
    for mask in range((p-1) ** K):
        B = [row[:] for row in A]
        temp = mask
        for idx in range(K):
            i, j = zeros[idx]
            B[i][j] = (temp % (p-1)) + 1
            temp //= (p-1)
        
        Bp = matpow(B, p, p)
        for i in range(N):
            for j in range(N):
                result[i][j] = (result[i][j] + Bp[i][j]) % p

for row in result:
    print(' '.join(map(str, row)))