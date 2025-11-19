def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    results = []
    
    MOD = 10**9 + 7
    
    for i in range(1, t + 1):
        a, b, k = map(int, data[i].split())
        n = (a + k - 1) // k + a
        m = (b + k - 1) // k + b
        
        results.append(f"{n % MOD} {m % MOD}")

    print("\n".join(results))

solve()