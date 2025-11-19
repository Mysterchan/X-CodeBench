def dfs(tree, node, parent, depth, depths, parents):
    depths[node] = depth
    for neighbor in tree[node]:
        if neighbor != parent:
            parents[neighbor] = node
            dfs(tree, neighbor, node, depth + 1, depths, parents)

def find_lca(u, v, parents, depths):
    while depths[u] > depths[v]:
        u = parents[u]
    while depths[v] > depths[u]:
        v = parents[v]
    while u != v:
        u = parents[u]
        v = parents[v]
    return u

def count_palindrome_pairs(n, tree, a):
    depths = [0] * (n + 1)
    parents = [0] * (n + 1)
    dfs(tree, 1, -1, 0, depths, parents)

    palindrome_count = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if a[i - 1][j - 1] == 1:
                lca = find_lca(i, j, parents, depths)
                path_length = depths[i] + depths[j] - 2 * depths[lca] + 1
                if path_length % 2 == 1:
                    palindrome_count += 1
                else:
                    mid = path_length // 2
                    if depths[i] - depths[lca] >= mid and depths[j] - depths[lca] >= mid:
                        palindrome_count += 1

    return palindrome_count

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    tree = [[] for _ in range(n + 1)]
    
    for i in range(1, n):
        u, v = map(int, data[i].split())
        tree[u].append(v)
        tree[v].append(u)
    
    a = [list(map(int, list(data[i + n - 1]))) for i in range(n)]
    
    # Check for non-palindrome pairs
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and i != j:
                print(10**100)
                return
    
    # Count palindrome pairs
    result = count_palindrome_pairs(n, tree, a)
    print(result)

if __name__ == "__main__":
    main()