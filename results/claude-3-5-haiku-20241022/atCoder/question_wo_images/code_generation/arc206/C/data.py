def is_good_sequence(B, N):
    # Check if sequence B is good
    for l in range(1, N+1):
        for r in range(l, N+1):
            valid = False
            for x in range(l, r+1):
                # Check if excluding position x makes [l,r] connected
                if check_interval(B, l, r, x, N):
                    valid = True
                    break
            if not valid:
                return False
    return True

def check_interval(B, l, r, x, N):
    # Check if vertices l..r form a tree when we add edges from i->B[i] for i in [l,r]\{x}
    # Build adjacency list for vertices l..r
    adj = {v: [] for v in range(l, r+1)}
    
    for i in range(l, r+1):
        if i == x:
            continue
        if B[i-1] < l or B[i-1] > r:
            return False
        adj[i].append(B[i-1])
        adj[B[i-1]].append(i)
    
    # Check if connected using BFS/DFS
    visited = set()
    stack = [l]
    visited.add(l)
    
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if u not in visited:
                visited.add(u)
                stack.append(u)
    
    return len(visited) == r - l + 1

def solve():
    N = int(input().split()[0])
    A = list(map(int, input().split()))
    
    MOD = 998244353
    
    # Find positions with -1
    unknown = [i for i in range(N) if A[i] == -1]
    
    if not unknown:
        return 1 if is_good_sequence(A, N) else 0
    
    count = 0
    # Try all possible values for unknowns
    def backtrack(idx):
        nonlocal count
        if idx == len(unknown):
            if is_good_sequence(A, N):
                count = (count + 1) % MOD
            return
        
        pos = unknown[idx]
        for val in range(1, N+1):
            A[pos] = val
            backtrack(idx + 1)
        A[pos] = -1
    
    backtrack(0)
    return count

print(solve())