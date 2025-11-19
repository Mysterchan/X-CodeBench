MOD = 10**9 + 7

def mod(x):
    return x % MOD

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    # We want the lexicographically minimum (n,m) such that any n x m matrix with elements in [1,k]
    # contains an a x b submatrix with all equal elements.
    #
    # Key insight:
    # Harshith tries to avoid such a submatrix.
    # Aryan wins if no matter how Harshith fills the matrix, there is always an a x b submatrix with all equal elements.
    #
    # This is a classic combinatorial problem related to the pigeonhole principle and the Erdős–Szekeres type arguments.
    #
    # The minimal n and m satisfy:
    # n = a + (k-1)*(a-1)
    # m = b + (k-1)*(b-1)
    #
    # Explanation:
    # To avoid an a x b submatrix of all equal elements, Harshith can try to arrange the matrix so that
    # for each color, the maximum number of rows with that color in a column is at most a-1,
    # and similarly for columns.
    #
    # So the minimal n and m that guarantee a monochromatic a x b submatrix is:
    # n = a + (k-1)*(a-1)
    # m = b + (k-1)*(b-1)
    #
    # This matches the sample outputs given.
    #
    # We output n and m modulo 10^9+7.

    n = a + (k - 1) * (a - 1)
    m = b + (k - 1) * (b - 1)

    print(mod(n), mod(m))