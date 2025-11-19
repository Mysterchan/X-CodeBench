def find_minimum_tuple(a, b, k):
    n = (a - 1) * k + 1
    m = (b - 1) * k + 1
    return n, m

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    MOD = 10**9 + 7
    
    for i in range(1, t + 1):
        a, b, k = map(int, data[i].split())
        n, m = find_minimum_tuple(a, b, k)
        results.append(f"{n % MOD} {m % MOD}")
    
    print("\n".join(results))

main()