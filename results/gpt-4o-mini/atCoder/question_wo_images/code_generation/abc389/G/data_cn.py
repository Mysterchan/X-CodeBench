def count_graphs(N, P):
    from math import comb

    if N % 2 != 0:
        return []

    results = []

    for M in range(N - 1, (N * (N - 1)) // 2 + 1):
        # Half vertices must be at even distance, and half must be at odd distance
        # Since N is even, we have to divide N by 2
        half_count = N // 2

        if M < N - 1 or M > (N * (N - 1)) // 2:
            results.append(0)
            continue
        
        # Calculate C(M, half_count) * (half_count - 1)^(N/2 - 1) * (half_count)^((N/2)) to count valid graphs
        if N == 2:
            results.append(0)
            continue

        # C(M, half_count) = M! / (half_count! * (M - half_count)!)
        total_graphs = comb(M, half_count)
        # Now we need to compute (half_count - 1)^(half_count - 1) * (half_count)^(half_count)
        even_parts = pow(half_count - 1, half_count - 1, P)
        odd_parts = pow(half_count, half_count, P)
        
        total_graphs = (total_graphs * even_parts) % P
        total_graphs = (total_graphs * odd_parts) % P
        
        results.append(total_graphs)

    return results

# Input reading
N, P = map(int, input().split())
# Function call and results printing
results = count_graphs(N, P)
print(" ".join(map(str, results)))