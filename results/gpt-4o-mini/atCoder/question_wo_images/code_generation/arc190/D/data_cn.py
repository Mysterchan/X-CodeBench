def matrix_power_mod(mat, exp, mod):
    n = len(mat)
    res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    while exp:
        if exp % 2 == 1:
            res = [[sum(res[i][k] * mat[k][j] for k in range(n)) % mod for j in range(n)] for i in range(n)]
        mat = [[sum(mat[i][k] * mat[k][j] for k in range(n)) % mod for j in range(n)] for i in range(n)]
        exp //= 2
    
    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, p = map(int, data[0].split())
    A = [list(map(int, line.split())) for line in data[1:N+1]]
    
    K = sum(1 for i in range(N) for j in range(N) if A[i][j] == 0)
    
    total_sum = [[0] * N for _ in range(N)]
    
    for mask in range(1 << K):
        B = [[0] * N for _ in range(N)]
        zero_index = 0
        
        for i in range(N):
            for j in range(N):
                if A[i][j] == 0:
                    B[i][j] = (mask >> zero_index) % (p - 1) + 1
                    zero_index += 1
                else:
                    B[i][j] = A[i][j]
        
        B_powered = matrix_power_mod(B, p, p)
        
        for i in range(N):
            for j in range(N):
                total_sum[i][j] = (total_sum[i][j] + B_powered[i][j]) % p
    
    for row in total_sum:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()