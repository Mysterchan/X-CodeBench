def dfs(node, parent):
    subtree_monsters[node] = monsters[node]
    for neighbor in tree[node]:
        if neighbor == parent:
            continue
        dfs(neighbor, node)
        subtree_monsters[node] += subtree_monsters[neighbor]

def calculate_paths():
    paths = 0
    for count in subtree_monsters[1:]:
        if count > 0:
            paths += 1
    return paths

def update_monsters(node):
    monsters[node] ^= 1
    subtree_monsters[node] += 1 if monsters[node] else -1
    for neighbor in tree[node]:
        if neighbor != parent[node]:
            update_monsters(neighbor)

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    output = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        global monsters, subtree_monsters, tree, parent
        monsters = list(map(int, data[idx].split()))
        monsters = [0] + monsters  # 1-indexed
        idx += 1
        
        tree = defaultdict(list)
        for __ in range(n - 1):
            u, v = map(int, data[idx].split())
            tree[u].append(v)
            tree[v].append(u)
            idx += 1
        
        queries = int(data[idx])
        idx += 1
        
        parent = [-1] * (n + 1)
        # Set up parent references using DFS
        def setup_parents(node, par):
            parent[node] = par
            for neighbor in tree[node]:
                if neighbor != par:
                    setup_parents(neighbor, node)
        
        setup_parents(1, -1)
        
        # We will need a list to count monsters in subtrees
        subtree_monsters = [0] * (n + 1)
        dfs(1, -1)
        
        # Initial calculation of paths
        output.append(calculate_paths())
        
        for __ in range(queries):
            v = int(data[idx])
            idx += 1
            
            update_monsters(v) 
            output.append(calculate_paths())
    
    sys.stdout.write("\n".join(map(str, output)) + "\n")

main()