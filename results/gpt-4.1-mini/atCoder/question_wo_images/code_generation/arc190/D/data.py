def main():
    import sys
    input = sys.stdin.readline

    N, p = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # Count zeros and prepare a matrix M where zeros are replaced by 1
    zero_positions = []
    M = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                zero_positions.append((i,j))
                M[i][j] = 1
            else:
                M[i][j] = A[i][j]

    K = len(zero_positions)
    # Number of matrices B is (p-1)^K

    # We want sum_{B} B^p mod p, where B differs from A only in zeros replaced by values in [1,p-1]

    # Key insight:
    # For prime p, by Fermat's little theorem:
    # For any x in [1, p-1], x^p ≡ x (mod p)
    # For zero entries replaced by x in [1,p-1], x^p ≡ x mod p
    #
    # Also, for matrices over field mod p:
    # (B)^p ≡ B^p mod p
    #
    # But we want sum over all B of B^p mod p.
    #
    # Using Freshman's dream (valid mod p):
    # (X+Y)^p ≡ X^p + Y^p mod p for matrices over field mod p
    #
    # But matrix addition and multiplication do not commute, so this doesn't hold for matrix powers.
    #
    # However, for matrices over field of char p, the Frobenius map (raising each element to p-th power) is a ring homomorphism.
    #
    # So (B)^p = (B^{[p]}) where B^{[p]} means raising each element of B to p-th power.
    #
    # Since B_{i,j}^p ≡ B_{i,j} mod p, we have B^p ≡ B^{[p]} = B mod p.
    #
    # So B^p ≡ B mod p.
    #
    # Therefore sum_{B} B^p ≡ sum_{B} B mod p.
    #
    # So the problem reduces to sum of all B matrices modulo p.
    #
    # For each zero position, the sum over all possible values in [1,p-1] is:
    # sum_{x=1}^{p-1} x = (p-1)*p/2 ≡ 0 mod p (since p divides numerator)
    #
    # So sum over all B of B_{i,j}:
    # - If A_{i,j} != 0, then B_{i,j} = A_{i,j} for all B, so sum over all B is A_{i,j} * (p-1)^K mod p
    # - If A_{i,j} == 0, then sum over all B of B_{i,j} = sum_{x=1}^{p-1} x * (p-1)^{K-1} = 0 mod p
    #
    # Since sum_{x=1}^{p-1} x ≡ 0 mod p, the sum for zero positions is 0 mod p.
    #
    # So final sum matrix S:
    # S_{i,j} = A_{i,j} * (p-1)^K mod p if A_{i,j} != 0
    # S_{i,j} = 0 if A_{i,j} == 0
    #
    # This matches the sample outputs.

    # Compute (p-1)^K mod p
    pow_val = pow(p-1, K, p)

    for i in range(N):
        row = []
        for j in range(N):
            if A[i][j] == 0:
                row.append(0)
            else:
                row.append((A[i][j] * pow_val) % p)
        print(*row)

if __name__ == "__main__":
    main()