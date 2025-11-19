def count_connected_graphs(N, P):
    from math import comb

    # Cache results
    results = [0] * (N * (N - 1) // 2 + 1)
    
    # Precompute the number of valid graphs for M edges
    for M in range(N-1, (N * (N - 1)) // 2 + 1):
        valid_graphs = 0
        
        for even_count in range(N // 2 + 1):
            if even_count * 2 == N:
                continue
            
            odd_count = N - even_count
            
            if (even_count + odd_count) != N:
                continue
            
            # We are only interested in the case of bipartite graphs
            count_bipartite_graphs = comb(N, even_count) * (1 << (even_count * odd_count))
            
            # Add the valid graphs to the result
            valid_graphs += count_bipartite_graphs

        # Store the result modulo P
        results[M] = valid_graphs % P
    
    return results[N-1:(N * (N-1)) // 2 + 1]

def main():
    import sys
    input = sys.stdin.read
    N, P = map(int, input().strip().split())
    results = count_connected_graphs(N, P)
    
    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()