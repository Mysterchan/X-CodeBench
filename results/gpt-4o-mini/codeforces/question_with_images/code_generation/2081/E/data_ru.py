MOD = 998244353

def factorial(n):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    return fact

def count_permutations(n, m, parent, colors, limits):
    # Count sizes of each subtree rooted at each node
    size = [0] * (n + 1)
    for i in range(n):
        size[parent[i]] += 1
    
    # Count colors in the range limits
    color_count = {}
    for i in range(m):
        max_depth = limits[i]
        color = colors[i]
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1
    
    # Each subtree can be arranged independently, we need arrangements of same colors
    total_permutations = 1
    for color in color_count:
        c = color_count[color]
        total_permutations *= factorial(c)
        total_permutations %= MOD
    
    # Total arrangements
    total_arrangements = factorial(m)
    total_arrangements *= pow(total_permutations, MOD - 2, MOD)  # Modular division
    total_arrangements %= MOD
    
    return total_arrangements

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    factorials = factorial(5000)  # Calculate all factorials up to 5000
    
    for _ in range(t):
        n, m = map(int, data[idx].split())
        idx += 1
        parent = list(map(int, data[idx].split()))
        idx += 1
        colors = list(map(int, data[idx].split()))
        idx += 1
        limits = list(map(int, data[idx].split()))
        idx += 1
        
        result = count_permutations(n, m, parent, colors, limits)
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

solve()