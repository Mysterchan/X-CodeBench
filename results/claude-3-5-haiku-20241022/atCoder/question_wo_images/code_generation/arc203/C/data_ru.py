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
        # Number of paths from top-left to bottom-right
        paths = comb(H + W - 2, H - 1, fact, inv_fact)
        print(paths)
    else:
        # K > min_walls
        paths = comb(H + W - 2, H - 1, fact, inv_fact)
        extra_walls = K - min_walls
        remaining_walls = total_walls - min_walls
        
        if extra_walls > remaining_walls:
            print(0)
        else:
            ways = comb(remaining_walls, extra_walls, fact, inv_fact)
            result = paths * ways % MOD
            print(result)