import sys
import math

def main():
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N, P = map(int, input().split())
    # N even, prime P

    # Problem restatement:
    # Count connected simple undirected graphs on N vertices (1..N),
    # with M edges (M from N-1 to N(N-1)/2),
    # such that the number of vertices at even distance from vertex 1
    # equals the number of vertices at odd distance from vertex 1.
    #
    # Output counts mod P for each M in ascending order.

    # Key observations:
    # - The graph is connected.
    # - The distance parity partition from vertex 1 splits vertices into two sets of equal size N/2.
    # - So the graph is bipartite with bipartition sizes N/2 and N/2, with vertex 1 in one part.
    # - The condition "number of vertices at even distance = number at odd distance" means the bipartition is balanced.
    #
    # So the graphs counted are connected bipartite graphs with bipartition sizes N/2 and N/2,
    # with vertex 1 in the "even" part.
    #
    # We want to count connected bipartite graphs with bipartition (N/2, N/2),
    # vertex 1 fixed in the first part, with exactly M edges.
    #
    # The maximum number of edges in bipartite graph K_{N/2,N/2} is (N/2)*(N/2) = N^2/4.
    #
    # M ranges from N-1 to N(N-1)/2.
    # But since the graph must be bipartite with parts of size N/2, max edges is N^2/4.
    # For N≥4, N^2/4 ≤ N(N-1)/2, so for M > N^2/4, answer is zero.
    #
    # So for M > N^2/4, output 0.
    #
    # For M < N-1, no connected graph.
    #
    # So effectively M in [N-1, N^2/4].
    #
    # We want number of connected bipartite graphs with bipartition (N/2,N/2) and M edges.
    #
    # The total number of bipartite graphs with bipartition (N/2,N/2) is 2^{N^2/4}.
    #
    # We want to count connected bipartite graphs with M edges.
    #
    # Approach:
    # Use exponential generating functions (EGF) or ordinary generating functions (OGF) for bipartite graphs.
    #
    # Let A(x) = sum_{k=0}^{N^2/4} C(N^2/4, k) x^k = (1+x)^{N^2/4} - generating function for all bipartite graphs.
    #
    # Let C(x) = generating function for connected bipartite graphs.
    #
    # Then A(x) = exp(C(x)) (exponential formula for graphs).
    #
    # So C(x) = log(A(x)).
    #
    # We want coefficients of C(x) modulo P.
    #
    # But we want connected bipartite graphs with bipartition fixed and vertex 1 in first part.
    #
    # The number of bipartite graphs with bipartition (N/2,N/2) is 2^{N^2/4}.
    #
    # The number of connected bipartite graphs with bipartition (N/2,N/2) is given by the coefficients of C(x).
    #
    # We want the number of connected bipartite graphs with exactly M edges.
    #
    # So:
    # - Compute A(x) = (1+x)^{N^2/4} mod P, coefficients up to degree N^2/4.
    # - Compute C(x) = log(A(x)) mod P.
    # - Output coefficients C_M for M in [N-1, N^2/4].
    #
    # For M > N^2/4, output 0.
    #
    # For M < N-1, output 0.
    #
    # Note: The problem states M from N-1 to N(N-1)/2.
    # For M > N^2/4, output 0.
    #
    # Implementation details:
    # - Compute binomial coefficients modulo P.
    # - Compute A(x) coefficients = C(N^2/4, k).
    # - Compute log(A(x)) modulo P using formal power series:
    #   log(A(x)) = integral(A'(x)/A(x)) dx
    #
    # Use polynomial operations modulo P.
    #
    # Since N ≤ 30, N^2/4 ≤ 225, so polynomial degree ≤ 225, manageable.
    #
    # Output answers for M = N-1 to N(N-1)/2:
    #   if M ≤ N^2/4: output C_M
    #   else: 0

    n = N
    half = n // 2
    max_edges_bipartite = half * half  # N^2/4

    max_M = n*(n-1)//2

    # Precompute factorials and inverse factorials modulo P for binomial coefficients
    max_deg = max_edges_bipartite

    fact = [1]*(max_deg+1)
    inv_fact = [1]*(max_deg+1)
    for i in range(1, max_deg+1):
        fact[i] = fact[i-1]*i % P

    # Fermat inverse
    inv_fact[max_deg] = pow(fact[max_deg], P-2, P)
    for i in reversed(range(max_deg)):
        inv_fact[i] = inv_fact[i+1]*(i+1) % P

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n]*inv_fact[k]%P*inv_fact[n-k]%P

    # A(x) = (1+x)^{max_edges_bipartite}
    # Coefficients: A_k = C(max_edges_bipartite, k)
    A = [comb(max_edges_bipartite, k) for k in range(max_edges_bipartite+1)]

    # Polynomial operations modulo P
    # We need to compute C(x) = log(A(x)) mod x^{max_deg+1}
    # log(A(x)) = integral(A'(x)/A(x)) dx
    # Steps:
    # 1) Compute A'(x)
    # 2) Compute invA(x) = inverse of A(x) mod x^{max_deg+1}
    # 3) Compute Q(x) = A'(x)*invA(x) mod x^{max_deg+1}
    # 4) Integrate Q(x) to get log(A(x))

    # Polynomial multiplication modulo x^{max_deg+1}
    def poly_mul(a, b):
        deg = max_deg
        res = [0]*(deg+1)
        for i in range(len(a)):
            ai = a[i]
            if ai == 0:
                continue
            for j in range(len(b)):
                if i+j > deg:
                    break
                res[i+j] = (res[i+j] + ai*b[j]) % P
        return res

    # Polynomial inverse modulo x^{max_deg+1} using Newton iteration
    # A[0] must be invertible mod P
    def poly_inv(f):
        deg = max_deg
        inv_f0 = pow(f[0], P-2, P)
        g = [inv_f0]
        length = 1
        while length <= deg:
            length <<= 1
            # f truncated to length
            f_len = f[:length]
            # g squared length
            g_len = g + [0]*(length - len(g))
            # compute g = g*(2 - f*g) mod x^{length}
            fg = poly_mul(f_len, g_len)
            fg = fg[:length]
            for i in range(length):
                fg[i] = (-fg[i]) % P
            fg[0] = (fg[0] + 2) % P
            g = poly_mul(g_len, fg)
            g = g[:length]
        return g[:deg+1]

    # Polynomial derivative
    def poly_derivative(f):
        deg = len(f)-1
        res = [0]*deg
        for i in range(1, len(f)):
            res[i-1] = f[i]*i % P
        return res

    # Polynomial integral
    inv = [0]*(max_deg+2)
    inv[1] = 1
    for i in range(2, max_deg+2):
        inv[i] = P - (P//i)*inv[P%i]%P

    def poly_integral(f):
        res = [0]*(len(f)+1)
        for i in range(len(f)):
            res[i+1] = f[i]*inv[i+1] % P
        return res

    A_der = poly_derivative(A)
    A_inv = poly_inv(A)
    Q = poly_mul(A_der, A_inv)
    Q = Q[:max_deg]

    C_poly = poly_integral(Q)
    C_poly = C_poly[:max_deg+1]

    # C_poly[k] = number of connected bipartite graphs with bipartition (N/2,N/2) and k edges modulo P

    # Output for M = N-1 to max_M:
    # if M > max_edges_bipartite: 0
    # if M < N-1: 0
    # else: C_poly[M]

    res = []
    for M in range(n-1, max_M+1):
        if M > max_edges_bipartite:
            res.append('0')
        else:
            res.append(str(C_poly[M] % P))

    print(' '.join(res))


if __name__ == "__main__":
    main()