MOD = 998244353

def modinv(a, m=MOD):
    # Fermat's little theorem for modular inverse since MOD is prime
    return pow(a, m-2, m)

def main():
    import sys
    input = sys.stdin.readline

    H, W = map(int, input().split())

    # The problem:
    # We consider all matrices obtainable by the operations:
    # - For any row r and column c, set A[r,1..c] = 1
    # - For any column c and row r, set A[1..r,c] = 1
    #
    # The set of obtainable matrices corresponds to all matrices A where
    # for each cell (i,j), A[i,j] = 1 if and only if i <= R_j or j <= C_i
    # for some non-decreasing sequences R_j and C_i.
    #
    # Actually, the problem is known to be equivalent to:
    # The set of matrices is in bijection with pairs of non-decreasing sequences:
    # R = (R_1 <= R_2 <= ... <= R_W), each R_j in [0,H]
    # C = (C_1 <= C_2 <= ... <= C_H), each C_i in [0,W]
    #
    # The matrix element A[i,j] = 1 if and only if i <= R_j or j <= C_i.
    #
    # We want sum over all such pairs (R,C) of sum of all A[i,j].
    #
    # The total number of such pairs is:
    # Number of non-decreasing sequences of length W with elements in [0,H] = C(H+W, W)
    # Number of non-decreasing sequences of length H with elements in [0,W] = C(W+H, H)
    # So total number of matrices = C(H+W, W)*C(H+W, H)
    #
    # We want sum over all pairs (R,C) of sum_{i=1}^H sum_{j=1}^W A[i,j].
    #
    # Let's define:
    # For fixed (R,C), sum of A[i,j] = sum over i,j of 1 if i <= R_j or j <= C_i else 0
    #
    # Using inclusion-exclusion:
    # A[i,j] = 1 - [i > R_j and j > C_i]
    #
    # So sum A[i,j] = H*W - sum_{i,j} [i > R_j and j > C_i]
    #
    # We want sum over all (R,C) of sum A[i,j] =
    # sum_{R,C} H*W - sum_{R,C} sum_{i,j} [i > R_j and j > C_i]
    # = (number_of_pairs)*H*W - sum_{i,j} sum_{R,C} [i > R_j and j > C_i]
    #
    # So we need to compute:
    # S = sum_{i=1}^H sum_{j=1}^W sum_{R,C} [i > R_j and j > C_i]
    #
    # Since R and C are independent sequences:
    # sum_{R,C} [i > R_j and j > C_i] = sum_R [i > R_j] * sum_C [j > C_i]
    #
    # For fixed i,j:
    # sum_R [i > R_j] = number of R with R_j < i
    # sum_C [j > C_i] = number of C with C_i < j
    #
    # We can compute these counts using combinatorics on non-decreasing sequences.
    #
    # Number of non-decreasing sequences of length n with elements in [0,M]:
    # total = C(M+n, n)
    #
    # Number of non-decreasing sequences with R_j < x:
    # R_j < x means R_j in [0, x-1]
    # The sequence is split into two parts:
    # - first j-1 elements <= R_j < x
    # - last W-j elements >= R_j
    #
    # The count is:
    # count_R_j_less_x = C(x + j -1, j) * C(H - x + W - j, W - j)
    #
    # Similarly for C_i < y:
    # count_C_i_less_y = C(y + i -1, i) * C(W - y + H - i, H - i)
    #
    # We sum over i,j:
    # S = sum_{i=1}^H sum_{j=1}^W count_R_j_less_i * count_C_i_less_j
    #
    # Then answer = total_pairs * H * W - S mod MOD
    #
    # Precompute factorials and inverse factorials for combinations.

    max_n = H + W + 10

    fact = [1]*(max_n)
    inv_fact = [1]*(max_n)
    for i in range(2, max_n):
        fact[i] = fact[i-1]*i % MOD
    inv_fact[-1] = modinv(fact[-1], MOD)
    for i in reversed(range(max_n-1)):
        inv_fact[i] = inv_fact[i+1]*(i+1) % MOD

    def comb(n,k):
        if k<0 or k>n:
            return 0
        return fact[n]*inv_fact[k]%MOD*inv_fact[n-k]%MOD

    # Precompute arrays for count_R_j_less_i and count_C_i_less_j

    # For fixed j and i:
    # count_R_j_less_i = C(i + j -1, j) * C(H - i + W - j, W - j)
    # For i in [1..H], j in [1..W]

    # For fixed i and j:
    # count_C_i_less_j = C(j + i -1, i) * C(W - j + H - i, H - i)

    # We'll precompute:
    # For all i,j:
    # count_R_j_less_i and count_C_i_less_j

    # To optimize, precompute:
    # For all i in [1..H], j in [1..W]:
    # C(i + j -1, j) and C(H - i + W - j, W - j)
    # C(j + i -1, i) and C(W - j + H - i, H - i)

    # Precompute all needed combinations in O(H+W) time by precomputing prefix arrays

    # We'll precompute arrays:
    # comb1[i][j] = C(i + j -1, j)
    # comb2[i][j] = C(H - i + W - j, W - j)
    # comb3[i][j] = C(j + i -1, i)
    # comb4[i][j] = C(W - j + H - i, H - i)

    # Since i and j can be up to 2*10^5, we cannot store full 2D arrays.
    # Instead, we compute on the fly inside loops.

    # We'll compute sum over i,j of:
    # count_R_j_less_i * count_C_i_less_j
    # = sum_{i=1}^H sum_{j=1}^W
    # [C(i + j -1, j) * C(H - i + W - j, W - j)] * [C(j + i -1, i) * C(W - j + H - i, H - i)]

    # Note that C(i + j -1, j) = C(i + j -1, i -1) (since C(n,k) = C(n,n-k))
    # Similarly, C(j + i -1, i) = C(i + j -1, i)

    # So C(i + j -1, j) * C(j + i -1, i) = C(i + j -1, i -1) * C(i + j -1, i)

    # Let's rewrite:

    # Let s = i + j -1

    # term = C(s, i -1) * C(H - i + W - j, W - j) * C(s, i) * C(W - j + H - i, H - i)

    # We'll iterate over i in [1..H], j in [1..W], compute term and sum.

    # To speed up, precompute factorials and use comb function.

    # Implement the sum carefully.

    total_pairs = comb(H+W, W)*comb(H+W, H) % MOD
    HW = H*W % MOD

    ans = total_pairs * HW % MOD

    S = 0
    for i in range(1, H+1):
        for j in range(1, W+1):
            s = i + j -1
            c1 = comb(s, i-1)
            c2 = comb(H - i + W - j, W - j)
            c3 = comb(s, i)
            c4 = comb(W - j + H - i, H - i)
            val = c1 * c2 % MOD
            val = val * c3 % MOD
            val = val * c4 % MOD
            S = (S + val) % MOD

    ans = (ans - S) % MOD
    print(ans)

if __name__ == "__main__":
    main()