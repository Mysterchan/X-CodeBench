MOD = 998244353

def power(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result

def modinv(a, mod):
    return power(a, mod - 2, mod)

H, W = map(int, input().split())

# 如果H和W都是奇数，不可能完成巡游
if H % 2 == 1 and W % 2 == 1:
    print(0)
else:
    # 总步数
    n = H * W
    
    # 需要n/2次向右，n/2次向左才能回到原点（列方向）
    # 使用Lucas定理或直接计算C(n, n/2)
    
    # 计算 C(n, n//2) mod MOD
    if n % 2 == 1:
        print(0)
    else:
        k = n // 2
        
        # 计算阶乘
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i-1] * i) % MOD
        
        # C(n, k) = n! / (k! * (n-k)!)
        result = fact[n]
        result = (result * modinv(fact[k], MOD)) % MOD
        result = (result * modinv(fact[n - k], MOD)) % MOD
        
        print(result)