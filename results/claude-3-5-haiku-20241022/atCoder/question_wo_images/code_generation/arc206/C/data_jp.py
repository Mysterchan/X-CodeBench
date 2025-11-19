def solve():
    MOD = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    
    # Find positions with -1
    unknowns = [i for i in range(N) if A[i] == -1]
    k = len(unknowns)
    
    def is_valid(B):
        # Check if sequence B is good
        for l in range(N):
            for r in range(l, N):
                valid = False
                for x in range(l, r + 1):
                    # Check if removing x makes [l,r] a tree
                    vertices = list(range(l, r + 1))
                    vertices.remove(x)
                    
                    if len(vertices) == 0:
                        valid = True
                        break
                    
                    # Check if all B[i] for i in vertices are in [l,r]
                    ok = True
                    for i in vertices:
                        if not (l <= B[i] <= r):
                            ok = False
                            break
                    
                    if not ok:
                        continue
                    
                    # Check connectivity using Union-Find
                    parent = {v: v for v in vertices}
                    
                    def find(v):
                        if parent[v] != v:
                            parent[v] = find(parent[v])
                        return parent[v]
                    
                    def union(u, v):
                        pu, pv = find(u), find(v)
                        if pu != pv:
                            parent[pu] = pv
                    
                    for i in vertices:
                        if B[i] != i and B[i] in vertices:
                            union(i, B[i])
                    
                    # Check if all vertices are connected
                    if len(vertices) > 0:
                        root = find(vertices[0])
                        if all(find(v) == root for v in vertices):
                            valid = True
                            break
                
                if not valid:
                    return False
        return True
    
    count = 0
    
    # Try all combinations
    def backtrack(idx, current):
        nonlocal count
        if idx == k:
            if is_valid(current):
                count = (count + 1) % MOD
            return
        
        pos = unknowns[idx]
        for val in range(1, N + 1):
            current[pos] = val
            backtrack(idx + 1, current[:])
            current[pos] = -1
    
    backtrack(0, A[:])
    print(count)

solve()