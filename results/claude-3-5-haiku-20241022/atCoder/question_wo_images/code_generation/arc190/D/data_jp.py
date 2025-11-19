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
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = [row[:] for row in A]
    
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_mult(result, base, p)
        base = matrix_mult(base, base, p)
        exp //= 2
    
    return result

def solve():
    N, p = map(int, input().split())
    A = []
    for _ in range(N):
        row = list(map(int, input().split()))
        A.append(row)
    
    zeros = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                zeros.append((i, j))
    
    K = len(zeros)
    
    result = [[0] * N for _ in range(N)]
    
    for mask in range((p - 1) ** K):
        B = [row[:] for row in A]
        temp = mask
        for idx in range(K):
            i, j = zeros[idx]
            B[i][j] = (temp % (p - 1)) + 1
            temp //= (p - 1)
        
        B_p = matrix_power(B, p, p)
        
        for i in range(N):
            for j in range(N):
                result[i][j] = (result[i][j] + B_p[i][j]) % p
    
    for i in range(N):
        print(' '.join(map(str, result[i])))

solve()