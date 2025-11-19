def dfs(tree, node, parent, depth, distances):
    distances[node] = depth
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(tree, neighbor, node, depth + 1, distances)


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
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
        for __ in range(n - 1):
            u, v = map(int, data[index].split())
            tree[u].append(v)
            tree[v].append(u)
            index += 1

        distances = [0] * (n + 1)
        dfs(tree, 1, -1, 0, distances)

        one_nodes = []
        for i in range(1, n + 1):
            if s[i - 1] == '1':
                one_nodes.append(i)

        m = len(one_nodes)
        answer = [-1] * n
        
        if m > 0:
            max_path_lengths = [0] * m
            next_index = [0] * m

            for i in range(m - 1, -1, -1):
                if i + 1 < m:
                    weights = []
                    for j in range(i + 1, m):
                        weight = distances[one_nodes[i]] + distances[one_nodes[j]] - 2 * distances[one_nodes[next_index[j]]]
                        if weight > max_path_lengths[i]:
                            max_path_lengths[i] = weight
                            weights.append((weight, j))
                    weights.sort()

                    current_length = 1
                    for weight, j in weights:
                        if weight >= 2 * next_index[i] or (weight == 0 and next_index[i] == 0):
                            current_length += 1
                            next_index[i] = j
                            if j + 1 < m and max_path_lengths[j + 1] >= next_index[j]:
                                next_index[j] = max_path_lengths[j + 1]

                answer[one_nodes[i]-1] = current_length

        results.append(" ".join(map(str, answer)))

    print("\n".join(results))


if __name__ == "__main__":
    main()