def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    MOD = 998244353
    results = []
    
    for k in range(1, N + 1):
        current_or = A[k - 1]
        product = 1
        for i in range(k):
            if (A[i] | current_or) == current_or:
                product = (product * A[i]) % MOD
        results.append(product)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()