def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    MOD = 998244353
    results = []
    
    for k in range(N):
        ak = A[k]
        product = 1
        
        for i in range(k + 1):
            if A[i] | ak == ak:
                product = (product * A[i]) % MOD
        
        results.append(product)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()