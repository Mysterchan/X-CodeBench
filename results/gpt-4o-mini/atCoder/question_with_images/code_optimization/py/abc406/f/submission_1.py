import sys
from collections import defaultdict

input = sys.stdin.readline

def dfs(node, parent):
    subtree_weight[node] = 1  # Each vertex initially has weight 1
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        subtree_sum[neighbor] = dfs(neighbor, node)
        subtree_weight[node] += subtree_sum[neighbor]
    return subtree_weight[node]

def main():
    global graph, subtree_weight, subtree_sum
    n = int(input())
    graph = defaultdict(list)

    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))

    # Initialize arrays
    subtree_weight = [0] * n
    subtree_sum = [0] * n

    # First DFS to calculate initial subtree weights
    dfs(0, -1)

    # Initial total weight of the tree
    total_weight = n  # Since all vertices start with weight 1

    q = int(input())
    output = []

    for _ in range(q):
        cmd = input().split()
        if cmd[0] == '1':
            x = int(cmd[1]) - 1
            w = int(cmd[2])
            # Increase the weight of vertex x
            subtree_weight[x] += w
            total_weight += w
        else:
            y = int(cmd[1]) - 1
            u, v = edges[y]

            # Determine which vertex is in the subtree when cutting edge y
            if subtree_weight[v] < subtree_weight[u]:
                # edge (u, v) means we are treating v as child
                sub_sum = subtree_weight[v]
            else:
                # edge (v, u) means we are treating u as child
                sub_sum = subtree_weight[u]
            
            # The difference in weights of the two components
            output.append(abs(total_weight - 2 * sub_sum))

    # Print all results for type '2' queries
    sys.stdout.write("\n".join(map(str, output)) + "\n")

if __name__ == "__main__":
    main()