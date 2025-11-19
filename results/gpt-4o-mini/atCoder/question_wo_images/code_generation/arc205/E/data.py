def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    MOD = 998244353
    results = []
    
    for k in range(1, N + 1):
        Ak = A[k - 1]
        product = 1
        
        for i in range(1, k + 1):
            if A[i - 1] | Ak == Ak:
                product = (product * A[i - 1]) % MOD
        
        results.append(product)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()