def process_queries(n, edges, queries):
    from collections import defaultdict
    import sys

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    results = []

    for l, r, k in queries:
        f_values = []
        for u in range(l, r + 1):
            f_value = 0
            for v in graph[u]:
                if l <= v <= r:
                    f_value ^= v
            f_values.append(f_value)

        f_values.sort()
        results.append(f_values[k - 1])

    return results


input = sys.stdin.read
data = input().splitlines()

idx = 0
t = int(data[idx])
idx += 1
results = []

for _ in range(t):
    n, m = map(int, data[idx].split())
    idx += 1
    edges = []
    for _ in range(m):
        u, v = map(int, data[idx].split())
        edges.append((u, v))
        idx += 1
    q = int(data[idx])
    idx += 1
    queries = []
    for _ in range(q):
        l, r, k = map(int, data[idx].split())
        queries.append((l, r, k))
        idx += 1

    results.extend(process_queries(n, edges, queries))

sys.stdout.write("\n".join(map(str, results)) + "\n")