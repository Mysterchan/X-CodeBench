import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, x, y, vx, vy = map(int, input().split())

        # The triangle vertices:
        # A = (0,0), B = (0,n), C = (n,0)
        # The airplane starts inside the triangle: x,y > 0 and x+y < n
        # Velocity vector: (vx, vy)

        # The airplane moves inside the triangle with reflections on edges:
        # Edges:
        # AB: x=0, y in [0,n]
        # AC: y=0, x in [0,n]
        # BC: x+y=n

        # Reflection rules:
        # When hitting AB (x=0), vx -> -vx, vy unchanged
        # When hitting AC (y=0), vy -> -vy, vx unchanged
        # When hitting BC (x+y=n), velocity reflected about line x+y=n
        # The normal vector to BC is (1,1)
        # Reflection formula for vector v about normal n:
        # v' = v - 2*(v·n)/(n·n)*n
        # Here n = (1,1), n·n=2
        # v·n = vx+vy
        # So vx' = vx - 2*(vx+vy)/2 = vx - (vx+vy) = -vy
        # vy' = vy - 2*(vx+vy)/2 = vy - (vx+vy) = -vx
        # So reflection on BC swaps and negates vx and vy:
        # (vx, vy) -> (-vy, -vx)

        # The airplane escapes if it reaches exactly one of the vertices (0,0), (0,n), (n,0)
        # We want to find if it ever reaches a vertex, and if yes, how many times it hits the boundary before that.

        # Approach:
        # The motion inside the triangle with reflections can be "unfolded" by reflecting the triangle and the path.
        # The airplane's position after time t without reflections is:
        # X(t) = x + vx * t
        # Y(t) = y + vy * t
        #
        # Because of reflections, the actual position inside the triangle can be found by folding the infinite plane
        # into the triangle using reflections.
        #
        # The key insight is to transform the problem into a lattice problem:
        # Define new coordinates:
        # u = x
        # v = y
        #
        # The triangle is defined by u >= 0, v >= 0, u + v <= n
        #
        # After reflections, the airplane's trajectory corresponds to a straight line in an extended lattice of triangles.
        #
        # The airplane escapes if there exists t >= 0 such that the airplane is at a vertex:
        # (0,0), (0,n), or (n,0)
        #
        # Because of reflections, the position modulo 2n in each coordinate with possible flipping.
        #
        # Let's consider the "billiard" unfolding:
        # The airplane moves in the plane with coordinates modulo 2n, with reflections modeled as:
        # For coordinate x:
        # pos_x(t) = (x + vx * t) mod (2n)
        # If pos_x(t) > n, pos_x(t) = 2n - pos_x(t)
        # Similarly for y:
        # pos_y(t) = (y + vy * t) mod (2n)
        # If pos_y(t) > n, pos_y(t) = 2n - pos_y(t)
        #
        # The airplane is inside the triangle if pos_x(t) >= 0, pos_y(t) >= 0, and pos_x(t) + pos_y(t) <= n
        #
        # The airplane escapes if pos_x(t), pos_y(t) is exactly one of the vertices:
        # (0,0), (0,n), (n,0)
        #
        # Because the airplane moves linearly, we want to find t >= 0 such that:
        # pos_x(t) in {0, n} and pos_y(t) in {0, n} and pos_x(t) + pos_y(t) in {0, n}
        #
        # The vertices correspond to:
        # (0,0), (0,n), (n,0)
        #
        # So we want to find t >= 0 such that:
        # pos_x(t) = 0 or n
        # pos_y(t) = 0 or n
        # and pos_x(t) + pos_y(t) = n or 0 (only vertices)
        #
        # Actually, vertices are only (0,0), (0,n), (n,0)
        # So pos_x(t), pos_y(t) must be one of these three points.
        #
        # Let's consider the "extended" coordinates without folding:
        # X(t) = x + vx * t
        # Y(t) = y + vy * t
        #
        # The folding is:
        # fx(t) = X(t) mod (2n)
        # if fx(t) > n: fx(t) = 2n - fx(t)
        # similarly for fy(t)
        #
        # We want fx(t), fy(t) to be one of the vertices.
        #
        # Let's define a function to get the "folded" coordinate:
        # fold(z) = z mod (2n)
        # if fold(z) > n: fold(z) = 2n - fold(z)
        #
        # So the problem reduces to finding t >= 0 such that:
        # fold(x + vx * t) = Xv in {0, n}
        # fold(y + vy * t) = Yv in {0, n}
        # and (Xv, Yv) in {(0,0), (0,n), (n,0)}
        #
        # Because fold(z) can be 0 or n only if z mod (2n) == 0 or n
        #
        # So for fold(x + vx * t) = 0:
        # (x + vx * t) mod (2n) == 0
        #
        # for fold(x + vx * t) = n:
        # (x + vx * t) mod (2n) == n
        #
        # Similarly for y.
        #
        # So for each vertex, we want to solve the system:
        # (x + vx * t) mod (2n) == Xv
        # (y + vy * t) mod (2n) == Yv
        #
        # where Xv, Yv in {0, n} and (Xv, Yv) in {(0,0), (0,n), (n,0)}
        #
        # We want to find the minimal t >= 0 satisfying these congruences.
        #
        # This is a system of two modular linear equations:
        # t * vx ≡ (Xv - x) mod 2n
        # t * vy ≡ (Yv - y) mod 2n
        #
        # We want to find t >= 0 satisfying both.
        #
        # If no such t exists, the airplane never reaches that vertex.
        #
        # We find the minimal t for each vertex and take the minimal among them.
        #
        # If no t found for any vertex, output -1.
        #
        # Once we find t, we can find how many times the airplane hits the boundary before that.
        #
        # The airplane hits the boundary when fold(x + vx * t) == 0 or n (but not vertex)
        # or fold(y + vy * t) == 0 or n (but not vertex)
        # or fold(x + vx * t) + fold(y + vy * t) == n (but not vertex)
        #
        # The number of hits before time t is the number of times the airplane hits the boundary before reaching the vertex.
        #
        # The hits correspond to times when the airplane hits the edges:
        # x=0 or x=n (folded coordinate 0 or n)
        # y=0 or y=n
        # x+y=n (folded sum)
        #
        # The times when fold(x + vx * t) == 0 or n are:
        # t such that (x + vx * t) mod (2n) == 0 or n
        #
        # Similarly for y.
        #
        # The times when the airplane hits the hypotenuse (x+y=n) correspond to:
        # fold(x + vx * t) + fold(y + vy * t) == n
        #
        # Because the folding is complicated, we can count hits by counting how many times the airplane hits each edge before time t.
        #
        # The hits on vertical edges (x=0 or x=n) occur at times:
        # t_x0: (x + vx * t) mod (2n) == 0
        # t_xn: (x + vx * t) mod (2n) == n
        #
        # Similarly for y.
        #
        # The hits on hypotenuse are more complicated, but since the airplane reflects on the hypotenuse by swapping and negating vx and vy,
        # the motion is symmetric.
        #
        # However, the problem states that each touch of the boundary counts, even if at the same point, but crossing a vertex does not count.
        #
        # So we count the number of hits on edges before time t, excluding the vertex time.
        #
        # The hits on edges occur periodically every (2n / gcd(vx, 2n)) for x edges and (2n / gcd(vy, 2n)) for y edges.
        #
        # For the hypotenuse, the period is more complicated, but we can count hits by simulating the sequence of hits in order.
        #
        # But simulation is impossible due to constraints.
        #
        # Instead, we use the fact that the airplane's motion in the unfolded plane is linear.
        #
        # The number of hits before time t is:
        # hits_x = number of times (x + vx * s) mod (2n) == 0 or n for s in [0, t)
        # hits_y = similarly for y
        # hits_hyp = number of times the airplane hits hypotenuse before t
        #
        # The total hits = hits_x + hits_y + hits_hyp
        #
        # But the airplane hits only one edge at a time (no simultaneous hits except vertices which don't count).
        #
        # So total hits = hits_x + hits_y + hits_hyp
        #
        # The times when (x + vx * t) mod (2n) == 0 or n are arithmetic progressions:
        # For 0:
        # t = (k * 2n - x) / vx for integer k such that t >= 0 and integer
        # For n:
        # t = (k * 2n + n - x) / vx
        #
        # Similarly for y.
        #
        # For hypotenuse:
        # The airplane hits hypotenuse when fold(x + vx * t) + fold(y + vy * t) == n
        #
        # This is complicated, but the problem is known and the number of hits before escape is:
        # hits = (t * (vx + vy)) // n - 1
        #
        # This formula comes from the problem editorial (known from similar problems).
        #
        # We will implement the solution using modular arithmetic and extended Euclidean algorithm to solve the congruences.

        # Helper functions:

        def extended_gcd(a, b):
            if b == 0:
                return a, 1, 0
            g, x1, y1 = extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return g, x, y

        def mod_inv(a, m):
            g, x, _ = extended_gcd(a, m)
            if g != 1:
                return None
            return x % m

        def solve_congruence(a, b, m):
            # Solve a * t ≡ b (mod m)
            # Returns minimal non-negative t or None if no solution
            g = 0
            g, x, y = extended_gcd(a, m)
            if b % g != 0:
                return None
            a1 = a // g
            b1 = b // g
            m1 = m // g
            x0 = (x * b1) % m1
            return x0

        # We want to solve for t:
        # t * vx ≡ (Xv - x) mod 2n
        # t * vy ≡ (Yv - y) mod 2n
        #
        # For each vertex (Xv, Yv) in {(0,0), (0,n), (n,0)}

        M = 2 * n

        vertices = [(0, 0), (0, n), (n, 0)]

        # For each vertex, find t satisfying both congruences
        # Use CRT to combine the two congruences

        def crt(a1, m1, a2, m2):
            # Solve system:
            # x ≡ a1 mod m1
            # x ≡ a2 mod m2
            # Returns (x mod lcm(m1,m2)) or None if no solution
            g, p, q = extended_gcd(m1, m2)
            if (a2 - a1) % g != 0:
                return None
            lcm = m1 // g * m2
            x = (a1 + (a2 - a1) // g * p % (m2 // g) * m1) % lcm
            return x, lcm

        ans = None

        for Xv, Yv in vertices:
            # Solve t * vx ≡ (Xv - x) mod M
            b1 = (Xv - x) % M
            t1 = solve_congruence(vx, b1, M)
            if t1 is None:
                continue
            # Solve t * vy ≡ (Yv - y) mod M
            b2 = (Yv - y) % M
            t2 = solve_congruence(vy, b2, M)
            if t2 is None:
                continue
            # Combine t ≡ t1 mod M and t ≡ t2 mod M
            res = crt(t1, M, t2, M)
            if res is None:
                continue
            t_candidate, mod_lcm = res
            # We want minimal t >= 0 satisfying this
            # t_candidate is already minimal non-negative modulo mod_lcm
            # So minimal t is t_candidate
            # But t_candidate can be 0, which means airplane starts at vertex (not possible since inside triangle)
            # So if t_candidate == 0, skip (no escape)
            if t_candidate == 0:
                continue
            if ans is None or t_candidate < ans:
                ans = t_candidate

        if ans is None:
            print(-1)
            continue

        # Count hits before time ans

        # Number of hits on vertical edges (x=0 or x=n):
        # times when (x + vx * t) mod M == 0 or n, t < ans
        # For each k:
        # t = (k * M - x) / vx if integer and t < ans
        # t = (k * M + n - x) / vx if integer and t < ans

        def count_hits(coord, v_coord):
            count = 0
            # For mod 0:
            # t = (k * M - coord) / v_coord
            # t >= 0 => k * M >= coord
            k_start = (coord + M - 1) // M  # smallest k with k*M >= coord
            # t < ans => (k * M - coord) / v_coord < ans
            # k * M < v_coord * ans + coord
            k_end = (v_coord * ans + coord - 1) // M
            if k_end >= k_start:
                count += k_end - k_start + 1

            # For mod n:
            # t = (k * M + n - coord) / v_coord
            # t >= 0 => k * M + n >= coord
            k_start = (coord - n + M - 1) // M
            if k_start < 0:
                k_start = 0
            # t < ans => (k * M + n - coord) / v_coord < ans
            # k * M < v_coord * ans + coord - n
            k_end = (v_coord * ans + coord - n - 1) // M
            if k_end >= k_start:
                count += k_end - k_start + 1
            return count

        hits_x = count_hits(x, vx)
        hits_y = count_hits(y, vy)

        # Count hits on hypotenuse (x+y=n)
        # The airplane hits hypotenuse when fold(x + vx * t) + fold(y + vy * t) == n
        #
        # The times when the airplane hits the hypotenuse correspond to:
        # t such that (x + vx * t) mod (2n) + (y + vy * t) mod (2n) == n or 3n
        #
        # Because fold(z) = z mod 2n if <= n else 2n - z mod 2n
        #
        # The sum fold(x) + fold(y) can be n only if:
        # (x + vx * t) mod (2n) + (y + vy * t) mod (2n) == n or 3n
        #
        # Let's define s(t) = (x + vx * t + y + vy * t) mod (2n) = (x + y + (vx + vy) * t) mod (2n)
        #
        # The airplane hits hypotenuse when fold(x + vx * t) + fold(y + vy * t) == n
        #
        # This happens when s(t) == n or s(t) == 3n (mod 2n)
        #
        # But 3n mod 2n = n (since 3n - 2n = n)
        #
        # So s(t) mod 2n == n
        #
        # So we want t such that:
        # (x + y + (vx + vy) * t) mod (2n) == n
        #
        # Solve for t:
        # (vx + vy) * t ≡ n - (x + y) mod 2n
        #
        # Count number of t < ans satisfying this congruence.

        b_hyp = (n - (x + y)) % M
        g = 0
        g, _, _ = extended_gcd(vx + vy, M)
        if b_hyp % g != 0:
            hits_hyp = 0
        else:
            # Step of solutions:
            step = M // g
            # One solution:
            t0 = solve_congruence(vx + vy, b_hyp, M)
            # Count number of solutions t = t0 + k * step < ans
            if t0 is None:
                hits_hyp = 0
            else:
                # t >= 0
                # k >= ceil((-t0)/step)
                k_start = 0 if t0 >= 0 else (-t0 + step - 1) // step
                # t < ans
                # t0 + k * step < ans
                # k < (ans - t0) / step
                k_end = (ans - t0 - 1) // step
                if k_end >= k_start:
                    hits_hyp = k_end - k_start + 1
                else:
                    hits_hyp = 0

        # The airplane escapes at time ans, which is a vertex, so the last hit is not counted.
        # So total hits before escape:
        total_hits = hits_x + hits_y + hits_hyp

        # But at time ans, the airplane is at vertex, so no hit counted at that moment.
        # Also, the airplane cannot hit two edges simultaneously except at vertex, so no double counting.

        print(total_hits)

if __name__ == "__main__":
    solve()