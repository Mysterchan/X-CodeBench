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
    
    half = matrix_power(A, exp // 2, p)
    result = matrix_mult(half, half, p)
    if exp % 2 == 1:
        result = matrix_mult(result, A, p)
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
    total_matrices = (p - 1) ** K
    
    result = [[0] * N for _ in range(N)]
    
    for mask in range(total_matrices):
        B = [row[:] for row in A]
        temp = mask
        for pos in zeros:
            val = temp % (p - 1) + 1
            temp //= (p - 1)
            B[pos[0]][pos[1]] = val
        
        B_power_p = matrix_power(B, p, p)
        
        for i in range(N):
            for j in range(N):
                result[i][j] = (result[i][j] + B_power_p[i][j]) % p
    
    for i in range(N):
        print(' '.join(map(str, result[i])))

solve()