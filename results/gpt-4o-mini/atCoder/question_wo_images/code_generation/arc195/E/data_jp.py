def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    idx = 0
    
    N = int(data[idx])
    Q = int(data[idx + 1])
    idx += 2
    
    A = list(map(int, data[idx:idx + N - 1]))
    idx += N - 1
    
    queries = []
    for _ in range(Q):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        queries.append((u, v))
        idx += 2
    
    # Precompute the contribution of each edge
    contribution = [0] * (N - 1)
    
    for i in range(1, N):
        contribution[i - 1] = A[i - 1] * (i + 1) * (N - i) % MOD
    
    # Precompute the total contribution for each query
    results = []
    for u, v in queries:
        if u > v:
            u, v = v, u
        
        total_distance = 0
        for i in range(u, v):
            total_distance = (total_distance + contribution[i]) % MOD
        
        results.append(total_distance)
    
    # Print results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()