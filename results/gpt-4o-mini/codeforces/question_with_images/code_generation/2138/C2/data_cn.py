def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        parents = list(map(int, data[idx:idx + n - 1]))
        idx += n - 1
        
        if k == 0:
            results.append(1)
            continue
        if k == n:
            results.append(1)
            continue
        
        # Number of leaves in the tree
        leaf_count = [0] * (n + 1)
        child_count = [0] * (n + 1)
        
        for p in parents:
            child_count[p] += 1
        
        for node in range(1, n + 1):
            if child_count[node] == 0:
                leaf_count[node] = 1
        
        total_leaves = sum(leaf_count)
        
        if k == 0 or k == n:
            results.append(1)
            continue
        
        # This will store the maximum beauty value
        max_beauty = min(total_leaves, k + 1)
        
        if max_beauty > total_leaves:
            max_beauty = total_leaves
        
        results.append(max_beauty)

    sys.stdout.write('\n'.join(map(str, results)) + '\n')

solve()