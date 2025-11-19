MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def solve():
    W, H, L, R, D, U = map(int, input().split())
    
    # Precompute factorials and inverse factorials
    max_n = W + H + 2
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = modinv(fact[max_n])
    for i in range(max_n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    
    def count_paths(x1, y1, x2, y2):
        # Count paths from (x1, y1) to (x2, y2) using only right and up moves
        if x2 < x1 or y2 < y1:
            return 0
        dx = x2 - x1
        dy = y2 - y1
        return comb(dx + dy, dx)
    
    def count_paths_in_rect(x1, y1, x2, y2):
        # Count all paths starting and ending in rectangle [x1, x2] x [y1, y2]
        if x1 > x2 or y1 > y2:
            return 0
        
        total = 0
        for sx in range(x1, x2 + 1):
            for sy in range(y1, y2 + 1):
                for ex in range(sx, x2 + 1):
                    for ey in range(sy, y2 + 1):
                        total = (total + count_paths(sx, sy, ex, ey)) % MOD
        return total
    
    # Total paths in the entire grid [0, W] x [0, H]
    total = count_paths_in_rect(0, 0, W, H)
    
    # Subtract paths that go through the hole [L, R] x [D, U]
    if L <= R and D <= U:
        # Paths entirely inside the hole
        inside = count_paths_in_rect(L, D, R, U)
        total = (total - inside) % MOD
        
        # Paths that enter and exit the hole
        for sx in range(0, W + 1):
            for sy in range(0, H + 1):
                # Skip if start is inside hole
                if L <= sx <= R and D <= sy <= U:
                    continue
                
                for ex in range(sx, W + 1):
                    for ey in range(sy, H + 1):
                        # Skip if end is inside hole
                        if L <= ex <= ey and D <= ey <= U:
                            continue
                        
                        # Check if path goes through hole
                        # A path from (sx, sy) to (ex, ey) goes through hole
                        # if there exists a point (hx, hy) in hole such that
                        # sx <= hx <= ex and sy <= hy <= ey
                        
                        if sx <= R and ex >= L and sy <= U and ey >= D:
                            # Calculate paths through hole using inclusion-exclusion
                            paths_through_hole = 0
                            
                            hx1 = max(L, sx)
                            hx2 = min(R, ex)
                            hy1 = max(D, sy)
                            hy2 = min(U, ey)
                            
                            if hx1 <= hx2 and hy1 <= hy2:
                                # Sum over all entry/exit points
                                for hx in range(hx1, hx2 + 1):
                                    for hy in range(hy1, hy2 + 1):
                                        paths_to = count_paths(sx, sy, hx, hy)
                                        paths_from = count_paths(hx, hy, ex, ey)
                                        paths_through_hole = (paths_through_hole + paths_to * paths_from) % MOD
                                
                                total_path = count_paths(sx, sy, ex, ey)
                                total = (total - paths_through_hole) % MOD
    
    print((total + MOD) % MOD)

solve()