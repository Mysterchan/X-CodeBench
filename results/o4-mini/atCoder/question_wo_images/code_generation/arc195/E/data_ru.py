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
    
    # Precompute the total weight contribution for each edge
    total_weight = [0] * (N - 1)
    
    for i in range(1, N):
        total_weight[i - 1] = A[i - 1] * (i) % MOD
    
    # Precompute the prefix sums of total_weight
    prefix_sum = [0] * (N - 1)
    prefix_sum[0] = total_weight[0]
    for i in range(1, N - 1):
        prefix_sum[i] = (prefix_sum[i - 1] + total_weight[i]) % MOD
    
    results = []
    
    for u, v in queries:
        if u > v:
            u, v = v, u
        
        # The distance between u and v is the sum of weights from u to v-1
        distance = prefix_sum[v - 1]
        if u > 0:
            distance = (distance - prefix_sum[u - 1]) % MOD
        
        results.append(distance)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()