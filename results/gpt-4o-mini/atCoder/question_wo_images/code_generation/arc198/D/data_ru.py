def dfs(node, parent):
    subtree_size[node] = 1
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            subtree_size[node] += subtree_size[neighbor]

def count_palindromic_pairs(node, parent):
    count = 0
    for neighbor in tree[node]:
        if neighbor != parent:
            count += count_palindromic_pairs(neighbor, node)
            count += subtree_size[neighbor] * (subtree_size[neighbor] - 1) // 2
    return count

import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
tree = defaultdict(list)
for i in range(1, N):
    u, v = map(int, data[i].split())
    tree[u].append(v)
    tree[v].append(u)

A = [list(map(int, list(data[i + N - 1]))) for i in range(N)]

subtree_size = [0] * (N + 1)
dfs(1, -1)

palindromic_pairs_count = count_palindromic_pairs(1, -1)

# Check for non-palindromic pairs
non_palindromic_found = False
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if A[i - 1][j - 1] == 1:
            # Check if (i, j) is a palindromic pair
            if i != j:
                # Check if the path from i to j is palindromic
                path = []
                # We can use a simple DFS or BFS to find the path from i to j
                # For simplicity, we will use a DFS approach to find the path
                def find_path(start, end, visited):
                    if start == end:
                        return [start]
                    visited.add(start)
                    for neighbor in tree[start]:
                        if neighbor not in visited:
                            result = find_path(neighbor, end, visited)
                            if result:
                                return [start] + result
                    return []
                
                path = find_path(i, j, set())
                if path:
                    is_palindrome = True
                    for k in range(len(path) // 2):
                        if path[k] != path[len(path) - 1 - k]:
                            is_palindrome = False
                            break
                    if not is_palindrome:
                        non_palindromic_found = True
                        break
    if non_palindromic_found:
        break

if non_palindromic_found:
    print(10**100)
else:
    print(palindromic_pairs_count + N)  # +N for (i, i) pairs