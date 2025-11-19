import sys

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        edges = [tuple(map(lambda x: int(x)-1, input().split())) for __ in range(m)]

        # Since each vertex can have degree at most 2,
        # the problem reduces to finding a maximum subgraph with max degree 2.
        # This is equivalent to finding a maximum matching in the line graph of G,
        # but since n is small and each vertex belongs to at most 5 simple cycles,
        # we can solve it efficiently by a maximum matching in a graph with degree constraints.

        # We model the problem as a maximum matching with degree constraints:
        # Each vertex can be matched up to 2 times (degree ≤ 2).
        # This is a maximum matching with vertex capacity constraints.

        # We can solve this by a flow network:
        # - Create a source and sink.
        # - For each vertex, create a node with capacity 2.
        # - For each edge, create an edge node connected to its two endpoints.
        # - Connect source to each edge node with capacity 1.
        # - Connect each vertex node to sink with capacity 2.
        # - Find max flow, which corresponds to max edges selected with degree ≤ 2.

        # Build flow network:
        # Nodes:
        # 0: source
        # 1..m: edge nodes
        # m+1..m+n: vertex nodes
        # m+n+1: sink

        size = m + n + 2
        source = 0
        sink = size - 1

        graph = [[] for _ in range(size)]

        def add_edge(u, v, cap):
            graph[u].append([v, cap, len(graph[v])])
            graph[v].append([u, 0, len(graph[u]) - 1])

        # source -> edge nodes (capacity 1)
        for i in range(m):
            add_edge(source, i+1, 1)

        # edge nodes -> vertex nodes (capacity 1)
        for i, (u, v) in enumerate(edges):
            add_edge(i+1, m+1+u, 1)
            add_edge(i+1, m+1+v, 1)

        # vertex nodes -> sink (capacity 2)
        for i in range(n):
            add_edge(m+1+i, sink, 2)

        # Dinic's max flow implementation
        level = [0]*size
        iter = [0]*size

        from collections import deque

        def bfs():
            for i in range(size):
                level[i] = -1
            level[source] = 0
            queue = deque([source])
            while queue:
                v = queue.popleft()
                for i, (to, cap, rev) in enumerate(graph[v]):
                    if cap > 0 and level[to] < 0:
                        level[to] = level[v] + 1
                        queue.append(to)
            return level[sink] != -1

        def dfs(v, upTo):
            if v == sink:
                return upTo
            while iter[v] < len(graph[v]):
                to, cap, rev = graph[v][iter[v]]
                if cap > 0 and level[v] < level[to]:
                    d = dfs(to, min(upTo, cap))
                    if d > 0:
                        graph[v][iter[v]][1] -= d
                        graph[to][rev][1] += d
                        return d
                iter[v] += 1
            return 0

        flow = 0
        INF = 10**9
        while bfs():
            for i in range(size):
                iter[i] = 0
            f = dfs(source, INF)
            while f > 0:
                flow += f
                f = dfs(source, INF)

        print(flow)

if __name__ == "__main__":
    main()