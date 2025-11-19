import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1

        tree = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = int(data[index]), int(data[index + 1])
            index += 2
            tree[u].append(v)
            tree[v].append(u)

        # BFS to calculate distances and prepare for nice path calculation
        def bfs(start):
            dist = [-1] * (n + 1)
            dist[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in tree[node]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
            return dist

        # Get distances from all nodes with '1'
        ones = [i for i in range(1, n + 1) if s[i - 1] == '1']
        distances = {i: bfs(i) for i in ones}

        # Calculate maximum nice path lengths
        max_nice_path = [-1] * (n + 1)

        for start in ones:
            path_length = 1
            current_weight = float('inf')
            current_node = start

            while True:
                next_node = -1
                for neighbor in ones:
                    if neighbor != current_node:
                        weight = distances[current_node][neighbor]
                        if weight > 0 and weight * 2 <= current_weight:
                            if next_node == -1 or distances[current_node][next_node] < weight:
                                next_node = neighbor

                if next_node == -1:
                    break

                path_length += 1
                current_weight = distances[current_node][next_node]
                current_node = next_node

            max_nice_path[start] = path_length

        results.append(' '.join(str(max_nice_path[i]) if s[i - 1] == '1' else '-1' for i in range(1, n + 1)))

    print('\n'.join(results))

if __name__ == "__main__":
    main()