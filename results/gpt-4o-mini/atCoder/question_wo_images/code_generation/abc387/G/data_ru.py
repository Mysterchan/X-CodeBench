def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_graphs(n):
    MOD = 998244353
    if n == 1:
        return 0  # A single vertex graph has no cycles

    # Calculate the number of edges in a complete graph with n vertices
    complete_graph_edges = n * (n - 1) // 2
    
    # Count the number of graphs that correspond to each possible number of edges
    count = 0
    
    # As cycles must have a prime number of edges
    for edges in range(1, complete_graph_edges + 1):
        if is_prime(edges):
            count += pow(2, complete_graph_edges - edges, MOD)  # 2^(total edges - edges in cycle)
            count %= MOD
    
    return count

import sys
input = sys.stdin.read

N = int(input().strip())
print(count_graphs(N))