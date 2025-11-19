from sys import stdin, stdout
from collections import defaultdict

input = stdin.read
data = input().split()
index = 0

def get_int():
    global index
    val = int(data[index])
    index += 1
    return val

t = get_int()
output = []

def dfs(node, parent):
    subtree_size = 0
    monster_count = 0
    for neighbor in tree[node]:
        if neighbor != parent:
            size, count = dfs(neighbor, node)
            subtree_size += size
            monster_count += count
    if monsters[node]:
        monster_count += 1
        disconnected.append(node)
    return subtree_size + 1, monster_count

def count_paths():
    global disconnected
    disconnected = []
    _, monster_count = dfs(1, -1)
    return len(disconnected)

def update_monster_status(v):
    stack = [v]
    while stack:
        node = stack.pop()
        monsters[node] = not monsters[node]
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

for _ in range(t):
    n = get_int()
    monsters = [False] + [x == 1 for x in map(int, data[index:index + n])]
    index += n
    tree = defaultdict(list)
    
    for __ in range(n - 1):
        u, v = get_int(), get_int()
        tree[u].append(v)
        tree[v].append(u)

    q = get_int()
    visited = [False] * (n + 1)
    initial_paths = count_paths()
    output.append(str(initial_paths))
    
    for __ in range(q):
        v = get_int()
        visited = [False] * (n + 1)
        visited[v] = True
        update_monster_status(v)
        output.append(str(count_paths()))

stdout.write("\n".join(output) + "\n")