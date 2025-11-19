MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def precompute_factorials(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (n + 1)
    inv_fact[n] = modinv(fact[n])
    for i in range(n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def solve(H, W, K):
    min_walls = H + W - 2
    max_walls = (H - 1) * W + (W - 1) * H
    
    if K < min_walls or K > max_walls:
        return 0
    
    max_n = max_walls + 10
    fact, inv_fact = precompute_factorials(max_n)
    
    total_h_walls = (H - 1) * W
    total_v_walls = H * (W - 1)
    total_walls = total_h_walls + total_v_walls
    
    result = 0
    
    for h in range(max(0, K - total_v_walls), min(total_h_walls, K) + 1):
        v = K - h
        if v < 0 or v > total_v_walls:
            continue
        
        ways_h = comb(total_h_walls, h, fact, inv_fact)
        ways_v = comb(total_v_walls, v, fact, inv_fact)
        ways_total = ways_h * ways_v % MOD
        
        min_h_needed = max(0, H - 1 - v)
        min_v_needed = max(0, W - 1 - h)
        
        if h < min_h_needed or v < min_v_needed:
            continue
        
        paths = 0
        for used_h in range(min_h_needed, h + 1):
            used_v = v - min_v_needed - (h - used_h)
            if used_v < 0 or used_v > v - min_v_needed:
                continue
            
            contrib = comb(h, used_h, fact, inv_fact) * comb(v, used_v + min_v_needed, fact, inv_fact) % MOD
            contrib = contrib * comb(used_h + used_v + min_h_needed + min_v_needed, used_h + min_h_needed, fact, inv_fact) % MOD
            paths = (paths + contrib) % MOD
        
        result = (result + ways_total * paths) % MOD
    
    return result

T = int(input())
for _ in range(T):
    H, W, K = map(int, input().split())
    print(solve(H, W, K))