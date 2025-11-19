def matrix_power_mod(mat, exp, mod):
    n = len(mat)
    res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    while exp:
        if exp % 2 == 1:
            res = matrix_mult_mod(res, mat, mod)
        mat = matrix_mult_mod(mat, mat, mod)
        exp //= 2
    
    return res

def matrix_mult_mod(A, B, mod):
    n = len(A)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = sum(A[i][k] * B[k][j] for k in range(n)) % mod
    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, p = map(int, data[0].split())
    A = [list(map(int, line.split())) for line in data[1:N+1]]
    
    K = sum(1 for i in range(N) for j in range(N) if A[i][j] == 0)
    
    # Calculate the contribution of each element
    result = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if A[i][j] != 0:
                result[i][j] = pow(A[i][j], p, p)
            else:
                # If A[i][j] is 0, we need to consider the contribution from all (p-1) choices
                result[i][j] = (p - 1) * (pow((p - 1) * (p - 1), K - 1, p) % p) % p
    
    # Now we need to raise the result matrix to the power of p
    final_result = matrix_power_mod(result, p, p)
    
    for row in final_result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()