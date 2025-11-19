MOD = 998244353

def modinv(a, m=MOD):
    # Fermat's little theorem for modular inverse since MOD is prime
    return pow(a, m-2, m)

def precompute_factorials(n, MOD):
    fact = [1] * (n+1)
    inv_fact = [1] * (n+1)
    for i in range(2, n+1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact[n] = modinv(fact[n], MOD)
    for i in reversed(range(1, n)):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    return fact, inv_fact

def comb(n, r, fact, inv_fact):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

def main():
    import sys
    input = sys.stdin.readline
    W, H, L, R, D, U = map(int, input().split())

    # The blocks are all points (x,y) with 0 <= x <= W, 0 <= y <= H,
    # except those inside the rectangle [L,R] x [D,U].
    # So blocks are in four regions:
    # 1) x < L
    # 2) x > R
    # 3) y < D
    # 4) y > U
    # Actually, the blocks are all points except those with L <= x <= R and D <= y <= U.

    # Snuke can start at any block and move only right or up to another block.
    # We want the number of possible paths modulo 998244353.

    # Key insight:
    # The town is a grid with a rectangular hole [L,R] x [D,U].
    # Paths can only move right or up, and must stay on blocks.
    # So paths cannot go through the hole.
    #
    # The number of paths from (x1,y1) to (x2,y2) with only right/up moves is:
    # C((x2 - x1) + (y2 - y1), x2 - x1)
    #
    # We want to count the number of all possible paths starting at any block and moving right/up on blocks.
    #
    # Let's consider the problem in terms of counting all pairs (start, end) with start <= end (coordinate-wise),
    # both start and end are blocks, and count the number of paths from start to end.
    #
    # The total number of paths is sum over all start and end blocks with start <= end of:
    # C((x2 - x1) + (y2 - y1), x2 - x1)
    #
    # But this is huge to compute directly.
    #
    # Instead, we use the principle of inclusion-exclusion and combinatorics.
    #
    # The problem is known and the formula for the answer is:
    #
    # Let:
    #   total_paths = number of paths in the full grid (0,0) to (W,H) starting anywhere and ending anywhere
    #   hole_paths = number of paths that go through the hole (L,D) to (R,U)
    #
    # The answer = total_paths - hole_paths
    #
    # But we must be careful because the hole is a rectangle of blocks removed.
    #
    # The problem reduces to:
    # Count all paths from any block to any block in the grid excluding the hole.
    #
    # The solution is:
    # sum over x in [0,W], y in [0,H] of number of paths starting at (x,y) and going to any block (x',y') with x' >= x, y' >= y,
    # both (x,y) and (x',y') are blocks.
    #
    # This can be computed by:
    #
    # sum over all blocks (x,y) of:
    #   number of blocks (x',y') with x' >= x, y' >= y
    #   times number of paths from (x,y) to (x',y')
    #
    # But this is complicated.
    #
    # Instead, the editorial approach (from the original AtCoder problem) is:
    #
    # The answer = sum over x in [0,L-1] of sum over y in [0,H] of C(W - x + H - y, W - x)
    #            + sum over x in [R+1,W] of sum over y in [0,H] of C(W - x + H - y, W - x)
    #            + sum over x in [L,R] of sum over y in [0,D-1] of C(W - x + H - y, W - x)
    #            + sum over x in [L,R] of sum over y in [U+1,H] of C(W - x + H - y, W - x)
    #
    # This counts all paths starting at blocks outside the hole and going to the top-right corner (W,H).
    #
    # But we want all paths starting anywhere and moving right/up on blocks.
    #
    # The problem is equivalent to:
    # The number of paths from any block to any block is equal to:
    # sum over all blocks (x,y) of number of paths from (x,y) to (W,H)
    #
    # Because any path from (x,y) to (x',y') can be extended to (W,H) by moving right/up,
    # and the number of paths from (x,y) to (W,H) includes all paths starting at (x,y).
    #
    # So the answer is sum over all blocks (x,y) of C((W - x) + (H - y), W - x).
    #
    # The blocks are all points except those inside the hole.
    #
    # So:
    # answer = sum_{x=0}^W sum_{y=0}^H C((W - x) + (H - y), W - x) - sum_{x=L}^R sum_{y=D}^U C((W - x) + (H - y), W - x)
    #
    # We can compute prefix sums to do this efficiently.
    #
    # Precompute factorials up to W+H.
    max_n = W + H
    fact, inv_fact = precompute_factorials(max_n, MOD)

    def c(n, r):
        return comb(n, r, fact, inv_fact)

    # Precompute prefix sums of C(i+j, i) for i in [0,W], j in [0,H]
    # Actually, we want sum over x,y of C((W - x) + (H - y), W - x)
    # Let's define f(x,y) = C((W - x) + (H - y), W - x)
    #
    # We want sum_{x=a}^b sum_{y=c}^d f(x,y)
    #
    # We can precompute prefix sums over x,y for f(x,y) for x in [0,W], y in [0,H].
    #
    # But W and H can be up to 10^6, so O(W*H) is impossible.
    #
    # We need a better approach.
    #
    # Note that f(x,y) = C((W - x) + (H - y), W - x) = C(s, t) where s = (W - x) + (H - y), t = W - x
    #
    # For fixed s, sum over t of C(s,t) = 2^s
    #
    # But we want sum over rectangles in (x,y).
    #
    # Let's change variables:
    # Let X = W - x, Y = H - y
    # Then x in [0,W] => X in [W,0]
    # y in [0,H] => Y in [H,0]
    #
    # So sum over x=a..b, y=c..d of f(x,y) =
    # sum over X in [W-b, W-a], Y in [H-d, H-c] of C(X + Y, X)
    #
    # So the rectangle in (X,Y) coordinates is:
    # X in [X1, X2] = [W-b, W-a]
    # Y in [Y1, Y2] = [H-d, H-c]
    #
    # We want sum_{X=X1}^{X2} sum_{Y=Y1}^{Y2} C(X+Y, X)
    #
    # Let's define S(n,m) = sum_{i=0}^n sum_{j=0}^m C(i+j, i)
    #
    # Then sum over rectangle [X1,X2] x [Y1,Y2] =
    # S(X2,Y2) - S(X1-1,Y2) - S(X2,Y1-1) + S(X1-1,Y1-1)
    #
    # So we need a formula for S(n,m).
    #
    # Let's find S(n,m):
    #
    # S(n,m) = sum_{i=0}^n sum_{j=0}^m C(i+j, i)
    #
    # We can rewrite:
    # sum_{j=0}^m C(i+j, i) = C(i+m+1, i+1)  (known combinatorial identity)
    #
    # So:
    # S(n,m) = sum_{i=0}^n C(i+m+1, i+1)
    #
    # Another identity:
    # sum_{i=0}^n C(i+k, i) = C(n+k+1, n)
    #
    # But here indices differ by 1.
    #
    # Let's try to find a closed form:
    #
    # sum_{i=0}^n C(i+m+1, i+1) = sum_{i=0}^n C(i+m+1, m+1) (since C(a,b) = C(a,a-b))
    #
    # So:
    # S(n,m) = sum_{i=0}^n C(i+m+1, m+1)
    #
    # sum_{i=0}^n C(i+k, k) = C(n+k+1, k+1)
    #
    # So:
    # S(n,m) = C(n+m+2, m+2)
    #
    # Let's verify for small values:
    # n=0,m=0: S(0,0) = C(0+0+2,0+2) = C(2,2) = 1
    # sum_{i=0}^0 sum_{j=0}^0 C(i+j,i) = C(0,0) = 1 correct.
    #
    # So the formula is:
    # S(n,m) = C(n+m+2, m+2)
    #
    # Great!
    #
    # So sum over rectangle [0..n] x [0..m] of C(i+j,i) = C(n+m+2, m+2)
    #
    # Then sum over rectangle [X1..X2] x [Y1..Y2] =
    # S(X2,Y2) - S(X1-1,Y2) - S(X2,Y1-1) + S(X1-1,Y1-1)
    #
    # where S(x,y) = C(x+y+2, y+2) if x,y >= 0 else 0
    #
    # Now we can compute the answer:
    #
    # answer = sum over all blocks (x,y) of f(x,y)
    #        = sum over (x,y) in [0,W]x[0,H] of f(x,y) - sum over (x,y) in [L,R]x[D,U] of f(x,y)
    #
    # Using (X,Y) = (W-x, H-y):
    #
    # sum over (x,y) in [a,b]x[c,d] of f(x,y) =
    # sum over X in [W-b, W-a], Y in [H-d, H-c] of C(X+Y, X)
    #
    # So:
    # total_sum = sum over X=0..W, Y=0..H of C(X+Y, X) = S(W,H) = C(W+H+2, H+2)
    #
    # hole_sum = sum over X in [W-R, W-L], Y in [H-U, H-D] of C(X+Y, X)
    #          = S(W-L, H-D) - S(W-R-1, H-D) - S(W-L, H-U-1) + S(W-R-1, H-U-1)
    #
    # Finally:
    # answer = total_sum - hole_sum (mod MOD)

    def S(n, m):
        if n < 0 or m < 0:
            return 0
        return c(n + m + 2, m + 2)

    total_sum = S(W, H)

    X1 = W - R
    X2 = W - L
    Y1 = H - U
    Y2 = H - D

    hole_sum = (S(X2, Y2) - S(X1 - 1, Y2) - S(X2, Y1 - 1) + S(X1 - 1, Y1 - 1)) % MOD

    ans = (total_sum - hole_sum) % MOD
    print(ans)

if __name__ == "__main__":
    main()