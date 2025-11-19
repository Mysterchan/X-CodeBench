MOD = 998244353

def count_valid_sequences(n, parents):
    from collections import defaultdict
    from math import factorial

    # Build the tree
    tree = defaultdict(list)
    for child, parent in enumerate(parents, start=2):
        tree[parent].append(child)

    # Calculate the size of each subtree
    subtree_size = [0] * (n + 1)

    def dfs(node):
        size = 1  # Count the current node
        for child in tree[node]:
            size += dfs(child)
        subtree_size[node] = size
        return size

    dfs(1)

    # Calculate the number of valid sequences
    result = 1
    for node in range(1, n + 1):
        if node in tree:
            children_count = len(tree[node])
            result *= factorial(subtree_size[node] - 1)  # (size of subtree - 1)!
            result %= MOD
            result *= pow(factorial(subtree_size[child] - 1) for child in tree[node])  # product of (size of each child subtree - 1)!
            result %= MOD

    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        parents = list(map(int, data[index:index + n - 1]))
        index += n - 1
        results.append(count_valid_sequences(n, parents))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()