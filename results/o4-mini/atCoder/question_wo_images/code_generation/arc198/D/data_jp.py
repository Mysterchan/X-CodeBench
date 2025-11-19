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

    # Function to find all pairs of nodes and their paths
    def bfs(start):
        parent = {start: None}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)
        return parent

    # Check if (i, j) is a palindrome pair
    def is_palindrome_pair(i, j):
        path = []
        # Find the path from i to j
        parent = bfs(i)
        current = j
        while current is not None:
            path.append(current)
            current = parent[current]
        return path == path[::-1]

    # Calculate the score
    palindrome_count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[i - 1][j - 1] == 1:
                if not is_palindrome_pair(i, j):
                    print(10**100)
                    return
            if is_palindrome_pair(i, j):
                palindrome_count += 1

    print(palindrome_count)

if __name__ == "__main__":
    main()