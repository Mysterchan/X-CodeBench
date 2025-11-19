def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n

        if sum(a) < n:
            results.append(0)
            continue
        
        result = 1
        total_cells = sum(a)
        
        for i in range(n):
            if a[i] > n - i:
                result = 0
                break
            result = result * factorial(n - i) % MOD
            result = result * mod_inv(factorial(a[i])) % MOD
        
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

def factorial(x):
    if x == 0:
        return 1
    res = 1
    for i in range(2, x + 1):
        res = res * i % MOD
    return res

def mod_inv(x):
    return pow(x, MOD - 2, MOD)

solve()