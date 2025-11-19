def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])
    edges = [tuple(map(int, line.split())) for line in data[1:N]]
    A = [list(map(int, list(data[i + N]))) for i in range(N)]
    
    # Build the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Function to find the depth and parent of each node using BFS
    def bfs(root):
        depth = [-1] * (N + 1)
        parent = [-1] * (N + 1)
        queue = deque([root])
        depth[root] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if depth[neighbor] == -1:  # Not visited
                    parent[neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    queue.append(neighbor)
        
        return depth, parent

    # Get depth and parent information
    depth, parent = bfs(1)

    # Function to find the path from u to v
    def find_path(u, v):
        path = []
        while u != v:
            if depth[u] > depth[v]:
                path.append(u)
                u = parent[u]
            else:
                path.append(v)
                v = parent[v]
        path.append(u)
        return path

    # Check for palindromic pairs
    palindromic_pairs_count = 0
    non_palindromic_found = False

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[i - 1][j - 1] == 1:
                path = find_path(i, j)
                if path != path[::-1]:  # Not a palindromic path
                    non_palindromic_found = True
                    break
                else:
                    palindromic_pairs_count += 1
        if non_palindromic_found:
            break

    if non_palindromic_found:
        print(10**100)
    else:
        print(palindromic_pairs_count)

if __name__ == "__main__":
    main()