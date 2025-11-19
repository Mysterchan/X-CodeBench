MOD = 998244353

def count_valid_sequences(n, parents):
    from collections import defaultdict
    from math import factorial

    # Build the tree
    tree = defaultdict(list)
    for child, parent in enumerate(parents, start=2):
        tree[parent].append(child)

    # Calculate the number of valid sequences
    def dfs(node):
        total_ways = 1
        total_children = 0
        
        for child in tree[node]:
            child_ways = dfs(child)
            total_ways *= child_ways
            total_children += 1
        
        # Calculate the number of ways to arrange the children
        if total_children > 0:
            total_ways *= factorial(total_children) % MOD
            total_ways %= MOD
        
        return total_ways

    return dfs(1)

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
        result = count_valid_sequences(n, parents)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()