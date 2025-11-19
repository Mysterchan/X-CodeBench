MOD = 998244353

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def solve(N):
    if N == 1:
        return 1
    
    # Предвычисляем факториалы
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact = [1] * (N + 1)
    inv_fact[N] = modinv(fact[N])
    for i in range(N - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # dp[n] = количество помеченных связных кактусов с простыми циклами на n вершинах
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    
    for n in range(2, N + 1):
        # Начинаем с дерева
        total = pow(n, n - 2, MOD) if n > 1 else 1
        
        # Добавляем графы с циклами
        for k in range(3, n + 1):
            if not is_prime(k):
                continue
            
            # Выбираем k вершин для цикла
            ways_to_choose = fact[n - 1] * inv_fact[k - 1] % MOD * inv_fact[n - k] % MOD
            
            # Число способов расположить оставшиеся вершины
            if n - k == 0:
                rest = 1
            else:
                rest = dp[n - k]
            
            # Число способов присоединить остальные вершины к циклу
            attach = pow(k, n - k, MOD)
            
            contribution = ways_to_choose * rest % MOD * attach % MOD
            total = (total + contribution) % MOD
        
        dp[n] = total
    
    return dp[N]

N = int(input())
print(solve(N))