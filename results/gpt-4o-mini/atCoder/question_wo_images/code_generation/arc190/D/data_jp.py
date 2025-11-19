def matrix_mult(A, B, p):
    N = len(A)
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(N)) % p
    return C

def matrix_pow(mat, exp, p):
    N = len(mat)
    res = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    while exp:
        if exp % 2 == 1:
            res = matrix_mult(res, mat, p)
        mat = matrix_mult(mat, mat, p)
        exp //= 2
    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, p = map(int, data[0].split())
    A = [list(map(int, line.split())) for line in data[1:N+1]]
    
    K = sum(row.count(0) for row in A)
    num_replacements = pow(p - 1, K, p)
    
    B = [[(A[i][j] if A[i][j] != 0 else 1) for j in range(N)] for i in range(N)]
    B_pow_p = matrix_pow(B, p, p)
    
    result = [[(B_pow_p[i][j] * num_replacements) % p for j in range(N)] for i in range(N)]
    
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()