import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

visited = [False]*(N+1)
res = 1

def dfs(u):
    stack = [u]
    nodes = 0
    deg_sum = 0
    visited[u] = True
    while stack:
        cur = stack.pop()
        nodes += 1
        deg_sum += len(edges[cur])
        for nxt in edges[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
    # deg_sum counts each edge twice
    E = deg_sum // 2
    V = nodes
    # Number of cycles in connected component = E - V + 1
    # Number of edge subsets forming cycles = 2^(number_of_cycles) - 1 (exclude empty)
    # But problem wants number of edge subsets that form simple cycles (each cycle corresponds to exactly one simple cycle)
    # Actually, each simple cycle corresponds to a unique cycle in the component.
    # The problem counts the number of simple cycles (cycles with distinct vertices).
    # In a connected component that is a simple cycle, number_of_cycles=1, subsets=1
    # But if multiple cycles, the problem counts all simple cycles, not all cycle subsets.
    # So we need to count the number of simple cycles in the component.
    # For a connected component that is a simple cycle, number_of_cycles=1, answer=1
    # For a tree, number_of_cycles=0, answer=0
    # For general graph, counting simple cycles is hard.
    # But the problem's sample and constraints hint that each connected component is either a simple cycle or a tree or a union of cycles.
    # The problem states: "找到 G 中的循環數量" means count the number of simple cycles.
    # The problem's explanation and sample show that the answer is the number of simple cycles in the graph.
    # For a connected component that is a simple cycle, number_of_cycles=1, answer=1
    # For a connected component that is a cycle plus chords, the number of simple cycles is more complex.
    # But the problem constraints N<=20, M up to 2e5, so the graph is large but vertices small.
    # So we can enumerate all simple cycles using backtracking with pruning.
    # But M is large, so we must process per connected component.
    # Since N<=20, we can do bitmask DP or backtracking per component.
    # So we collect nodes in the component and edges in the component, then enumerate all simple cycles.
    return V,E

# Collect connected components
components = []
visited = [False]*(N+1)
for i in range(1,N+1):
    if not visited[i]:
        stack = [i]
        comp_nodes = []
        visited[i] = True
        while stack:
            u = stack.pop()
            comp_nodes.append(u)
            for w in edges[u]:
                if not visited[w]:
                    visited[w] = True
                    stack.append(w)
        components.append(comp_nodes)

# For each component, enumerate all simple cycles and count them
# Since N<=20, we can do backtracking to find all simple cycles in each component
# To avoid duplicates, we use a standard approach:
# - For each node u in component, do DFS to find all simple cycles starting at u with nodes > u to avoid duplicates
# - Use path and visited set to track current path
# - When we find a back edge to start node, record cycle
# - Use a set to store cycles as sorted tuple of nodes to avoid duplicates

def count_cycles(comp):
    comp_set = set(comp)
    adj = {u:[] for u in comp}
    for u in comp:
        for w in edges[u]:
            if w in comp_set:
                adj[u].append(w)
    cycles = set()
    n = len(comp)
    comp_sorted = sorted(comp)
    index = {v:i for i,v in enumerate(comp_sorted)}

    def dfs(start, u, visited, path):
        for w in adj[u]:
            if w == start and len(path) >= 2:
                # found a cycle
                cycle_nodes = tuple(sorted(path))
                cycles.add(cycle_nodes)
            elif w > start and w not in visited:
                visited.add(w)
                path.append(w)
                dfs(start, w, visited, path)
                path.pop()
                visited.remove(w)

    for u in comp_sorted:
        dfs(u, u, {u}, [u])
    return len(cycles) % MOD

ans = 0
for comp in components:
    ans += count_cycles(comp)
ans %= MOD

print(ans)