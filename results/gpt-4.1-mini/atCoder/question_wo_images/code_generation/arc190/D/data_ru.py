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

def main():
    N, p = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # Count zeros and prepare matrix C = A with zeros replaced by 1
    zero_positions = []
    C = [row[:] for row in A]
    for i in range(N):
        for j in range(N):
            if C[i][j] == 0:
                zero_positions.append((i,j))
                C[i][j] = 1

    K = len(zero_positions)
    # Number of matrices B is (p-1)^K

    # Compute C^p mod p
    Cp = matpow(C, p, p)

    # Compute S = sum_{x=1}^{p-1} x^p mod p
    # By Fermat's little theorem: for x not divisible by p, x^p ≡ x mod p
    # So sum_{x=1}^{p-1} x^p ≡ sum_{x=1}^{p-1} x mod p = (p-1)*p/2 mod p = 0
    # But we need the exact sum mod p:
    # sum_{x=1}^{p-1} x = (p-1)*p/2 ≡ 0 mod p
    # So S = 0 mod p

    # However, if p=2, sum_{x=1}^{1} x^2 = 1^2=1 mod 2
    # Let's compute S carefully:
    # sum_{x=1}^{p-1} x^p mod p = sum_{x=1}^{p-1} x mod p = (p-1)*p/2 mod p = 0
    # So S=0 mod p for all p>2
    # For p=2, sum_{x=1}^{1} x^2 = 1 mod 2 =1
    # So:
    if p == 2:
        S = 1
    else:
        S = 0

    # If K=0 (no zeros), then sum over B is just C^p
    if K == 0:
        for i in range(N):
            print(' '.join(str(x % p) for x in Cp[i]))
        return

    # Now, sum over all B of B^p mod p
    # Using Freshman's theorem in char p: (C + D)^p = C^p + D^p mod p
    # Each B = C + sum over zero positions of (b_{i,j}-1)*E_{i,j}
    # So B^p = C^p + sum over zero positions of (b_{i,j}-1)^p * E_{i,j}^p mod p
    # But E_{i,j}^p = E_{i,j} (since E_{i,j} is a matrix with one 1)
    # So B^p = C^p + sum over zero positions of (b_{i,j}-1)*E_{i,j} mod p

    # Sum over all B:
    # sum_B B^p = sum_B C^p + sum_B sum_{(i,j)} (b_{i,j}-1)*E_{i,j}
    # = (p-1)^K * C^p + sum_{(i,j)} E_{i,j} * sum_B (b_{i,j}-1)

    # sum_B (b_{i,j}-1) = (p-1)^{K-1} * sum_{x=1}^{p-1} (x-1)
    # sum_{x=1}^{p-1} (x-1) = sum_{y=0}^{p-2} y = (p-2)(p-1)/2 mod p

    # Compute sum_{x=1}^{p-1} (x-1) mod p
    # = (p-2)*(p-1)//2 mod p
    # Let's compute carefully:
    # (p-2)*(p-1)//2 mod p
    # Since p is prime, inverse of 2 mod p exists if p != 2
    # For p=2, (p-2)*(p-1)//2 = 0

    if p == 2:
        sum_x_minus_1 = 0
    else:
        inv2 = (p + 1) // 2  # modular inverse of 2 mod p for odd prime p
        sum_x_minus_1 = ((p - 2) * (p - 1) * inv2) % p

    # total number of B: (p-1)^K mod p
    # We need to compute (p-1)^K mod p
    # Since p is prime, (p-1) ≡ -1 mod p
    # So (p-1)^K ≡ (-1)^K mod p
    total_B = pow(p - 1, K, p)

    # sum_B (b_{i,j}-1) = total_B / (p-1) * sum_x_minus_1 mod p
    # total_B / (p-1) mod p = total_B * inv(p-1) mod p
    # inv(p-1) mod p = inv(-1) = -1 mod p = p-1

    inv_p_minus_1 = p - 1
    sum_bij_minus_1 = (total_B * inv_p_minus_1) % p
    sum_bij_minus_1 = (sum_bij_minus_1 * sum_x_minus_1) % p

    # Now build the result matrix:
    # result = total_B * C^p + for each zero position (i,j): sum_bij_minus_1 * E_{i,j}
    # For non-zero positions, just total_B * Cp[i][j]
    # For zero positions, add sum_bij_minus_1

    res = [[(total_B * Cp[i][j]) % p for j in range(N)] for i in range(N)]
    for (i,j) in zero_positions:
        res[i][j] = (res[i][j] + sum_bij_minus_1) % p

    for i in range(N):
        print(' '.join(map(str, res[i])))

if __name__ == "__main__":
    main()