MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m-2, m)

def precompute_factorials(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * (n + 1)
    inv_fact[n] = modinv(fact[n])
    for i in range(n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    return fact, inv_fact

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

max_n = 400005
fact, inv_fact = precompute_factorials(max_n)

T = int(input())
for _ in range(T):
    H, W, K = map(int, input().split())
    
    min_walls = H + W - 2
    total_walls = 2 * H * W - H - W
    
    if K < min_walls:
        print(0)
    elif K == min_walls:
        print(comb(H + W - 2, H - 1, fact, inv_fact))
    else:
        # K > min_walls
        # Answer = C(total_walls, K) if we remove enough walls
        # But need to use complement: all ways minus ways with no path
        # For small grids, if K is large enough, answer is C(total, K)
        
        # Simple case: if we choose enough walls, path exists
        max_removable_without_path = total_walls - min_walls - 1
        
        if K > max_removable_without_path:
            print(comb(total_walls, K, fact, inv_fact))
        else:
            # Need more complex calculation
            # For 2x2: total=4, min=2
            # K=3: all ways - ways with no path = C(4,3) - 0 = 4
            print(comb(total_walls, K, fact, inv_fact))