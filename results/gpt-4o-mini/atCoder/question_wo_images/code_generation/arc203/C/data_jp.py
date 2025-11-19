def mod_comb(n, k, mod):
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    num = den = 1
    for i in range(k):
        num = num * (n - i) % mod
        den = den * (i + 1) % mod
    return num * pow(den, mod - 2, mod) % mod

def solve_case(H, W, K):
    mod = 998244353
    total_walls = (H - 1) + (W - 1)
    
    if K > total_walls:
        return 0
    
    if K < (H + W - 2):
        return 0
    
    if K == (H + W - 2):
        return 1
    
    # Calculate the number of ways to choose K walls from total_walls
    return mod_comb(total_walls, K, mod)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        H = int(data[index])
        W = int(data[index + 1])
        K = int(data[index + 2])
        index += 3
        
        result = solve_case(H, W, K)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()