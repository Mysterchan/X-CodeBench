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
    
    # Precompute the total contribution of each edge
    total_contribution = [0] * (N - 1)
    
    # Each edge A[i] contributes to the distance between all pairs (u, v) where u < i+2 < v
    for i in range(N - 1):
        # The edge A[i] connects node i+2 to its parent P[i]
        # It contributes to all pairs (u, v) where u < i+2 < v
        # u can be from 1 to i+1 (i+1 choices)
        # v can be from i+3 to N (N - (i + 2) choices)
        left_choices = i + 1
        right_choices = N - (i + 2)
        total_contribution[i] = (left_choices * right_choices) % MOD
    
    # Now we can answer each query
    results = []
    for u, v in queries:
        if u > v:
            u, v = v, u
        
        # The distance between u and v is the sum of contributions of edges A[i] for i in range(u, v-1)
        distance_sum = 0
        for i in range(u, v - 1):
            distance_sum += (total_contribution[i] * A[i]) % MOD
            distance_sum %= MOD
        
        results.append(distance_sum)
    
    # Print all results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()