import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index]); index += 1
        a = [0] * (n+1)
        for i in range(1, n+1):
            a[i] = int(data[index]); index += 1
        graph = [[] for _ in range(n+1)]
        for i in range(n-1):
            u = int(data[index]); v = int(data[index+1]); index += 2
            graph[u].append(v)
            graph[v].append(u)

        f = [0] * (n+1)
        h = [0] * (n+1)
        parent = [0] * (n+1)
        stack = [1]
        order = []
        visited = [False] * (n+1)
        visited[1] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
        for u in reversed(order):
            f[u] = a[u]
            h[u] = -a[u]
            for v in graph[u]:
                if v == parent[u]:
                    continue
                f[u] = max(f[u], a[u] + h[v])
                h[u] = max(h[u], -a[u] + f[v])
        res = [str(f[i]) for i in range(1, n+1)]
        output_lines.append(" ".join(res))
        visited = [False] * (n+1)
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()
