import sys
input = sys.stdin.readline

MOD = 10**9 + 7

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    # We have a bipartite grid coloring pattern:
    # color(i,j) = color_parity ^ ((i+j) % 2)
    # We want to find number of ways to assign color_parity in {0,1}
    # so that all given fixed cells' colors are consistent.
    # If no solution, answer = 0
    # If one solution, answer = 2^(number_of_unfixed_cells)
    # But since n,m large, we only count degrees of freedom:
    # The coloring is determined by color_parity (0 or 1).
    # For each fixed cell (x,y,c):
    # c = color_parity ^ ((x+y)%2)
    # So color_parity = c ^ ((x+y)%2)
    # If conflicting color_parity from fixed cells, no solution.
    # Otherwise, 2^(number_of_unfixed_cells) = 2^(n*m - k)
    # But we must ensure the number of edges with different colors is even.
    #
    # The problem states: after painting, the number of edges with different colors is even.
    #
    # Key insight:
    # The number of edges with different colors in a bipartite checkerboard coloring:
    # For the coloring defined by color_parity:
    # The number of edges with different colors is always n*(m-1) + (n-1)*m
    # because edges connect cells of different parity.
    #
    # But the problem states the count of edges with different colors must be even.
    # Let's analyze parity of total edges:
    # total edges = n*(m-1) + (n-1)*m = 2*n*m - n - m
    # The parity of total edges:
    # total_edges % 2 = (2*n*m - n - m) % 2 = (-n - m) % 2 = (n + m) % 2
    #
    # For checkerboard coloring, all edges connect different parity cells,
    # so all edges are between different colors.
    # So number of edges with different colors = total edges.
    #
    # So number of edges with different colors parity = (n + m) % 2
    #
    # We want this number to be even, so (n + m) % 2 == 0
    #
    # If (n + m) % 2 == 1, no solution.
    #
    # Now, the fixed cells impose constraints on color_parity:
    # For each fixed cell (x,y,c):
    # color_parity = c ^ ((x+y)%2)
    #
    # If multiple fixed cells impose conflicting color_parity, no solution.
    #
    # If consistent, number of ways = 2^(number_of_unfixed_cells)
    # = 2^(n*m - k) mod MOD
    #
    # But n*m can be huge (up to 10^18), so we must use fast exponentiation.
    #
    # Implementation:
    # 1. Check parity of (n + m)
    # 2. If odd, print 0
    # 3. Else, check fixed cells constraints on color_parity
    # 4. If conflict, print 0
    # 5. Else print pow(2, n*m - k, MOD)
    #
    # Since n*m can be large, use pow with modulo.
    #
    # Note: n*m - k can be large, but pow supports large exponents.
    #
    # Edge case: if k == n*m (all cells fixed), then ways = 1 if consistent else 0.
    #
    # Let's implement.

    if (n + m) % 2 == 1:
        # number of edges with different colors is odd, no solution
        # because all edges connect different parity cells, so all edges differ in color
        # so |A| = total edges = odd, contradicts requirement even
        # so answer = 0
        for __ in range(k):
            input()  # discard fixed cells
        print(0)
        continue

    color_parity = -1
    conflict = False
    for __ in range(k):
        x, y, c = map(int, input().split())
        val = c ^ ((x + y) % 2)
        if color_parity == -1:
            color_parity = val
        elif color_parity != val:
            conflict = True
    if conflict:
        print(0)
        continue

    # number of ways = 2^(n*m - k) mod MOD
    # n*m can be large, so use pow with modulo
    # n*m - k might be large, but pow supports it
    # compute exponent = (n*m - k) mod (MOD-1) due to Fermat's little theorem for exponentiation cycles
    # but since MOD is prime, exponent mod (MOD-1) is needed for pow base MOD
    # However, n*m can be up to 10^18, so we must do modulo (MOD-1) for exponent

    exp = ((n % (MOD - 1)) * (m % (MOD - 1))) % (MOD - 1)
    exp = (exp - k) % (MOD - 1)
    ans = pow(2, exp, MOD)
    print(ans)