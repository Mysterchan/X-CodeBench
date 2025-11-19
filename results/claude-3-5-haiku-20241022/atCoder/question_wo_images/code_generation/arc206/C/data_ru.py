def solve():
    MOD = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    
    # Convert to 0-indexed
    A = [a - 1 if a != -1 else -1 for a in A]
    
    def is_valid_sequence(seq):
        # Check if sequence is good
        n = len(seq)
        for l in range(n):
            for r in range(l, n):
                # Check if there exists x such that removing edge from x makes vertices l..r connected
                found = False
                for x in range(l, r + 1):
                    # Build graph without edge from x
                    parent = list(range(n))
                    
                    def find(u):
                        if parent[u] != u:
                            parent[u] = find(parent[u])
                        return parent[u]
                    
                    def union(u, v):
                        pu, pv = find(u), find(v)
                        if pu != pv:
                            parent[pu] = pv
                    
                    for i in range(l, r + 1):
                        if i != x and l <= seq[i] <= r:
                            union(i, seq[i])
                    
                    # Check if all vertices in [l, r] are connected
                    root = find(l)
                    connected = all(find(i) == root for i in range(l, r + 1))
                    if connected:
                        found = True
                        break
                
                if not found:
                    return False
        return True
    
    def generate(pos, current):
        if pos == N:
            if is_valid_sequence(current):
                return 1
            return 0
        
        if A[pos] != -1:
            return generate(pos + 1, current + [A[pos]])
        
        count = 0
        for val in range(N):
            count = (count + generate(pos + 1, current + [val])) % MOD
        return count
    
    result = generate(0, [])
    print(result)

solve()