def matrix_mult(A, B, p):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % p
    return C

def matrix_power(A, exp, p):
    n = len(A)
    if exp == 0:
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            result[i][i] = 1
        return result
    if exp == 1:
        return [row[:] for row in A]
    
    if exp % 2 == 0:
        half = matrix_power(A, exp // 2, p)
        return matrix_mult(half, half, p)
    else:
        return matrix_mult(A, matrix_power(A, exp - 1, p), p)

def solve():
    n, p = map(int, input().split())
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        A.append(row)
    
    zeros = []
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:
                zeros.append((i, j))
    
    k = len(zeros)
    
    result = [[0] * n for _ in range(n)]
    
    for mask in range((p - 1) ** k):
        B = [row[:] for row in A]
        temp = mask
        for idx in range(k):
            i, j = zeros[idx]
            val = (temp % (p - 1)) + 1
            B[i][j] = val
            temp //= (p - 1)
        
        Bp = matrix_power(B, p, p)
        
        for i in range(n):
            for j in range(n):
                result[i][j] = (result[i][j] + Bp[i][j]) % p
    
    for i in range(n):
        print(' '.join(map(str, result[i])))

solve()