import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def range_sum(self, l, r):
        return self.query(r - 1) - self.query(l - 1)

def dfs(u, p, graph, in_time, out_time, timer):
    in_time[u] = timer[0]
    timer[0] += 1
    for v in graph[u]:
        if v != p:
            dfs(v, u, graph, in_time, out_time, timer)
    out_time[u] = timer[0]

def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))

    in_time = [0] * n
    out_time = [0] * n
    timer = [0]
    dfs(0, -1, graph, in_time, out_time, timer)

    fenw = FenwickTree(n)
    for i in range(n):
        fenw.add(in_time[i], 1)

    total = n
    q = int(input())
    output = []
    for _ in range(q):
        cmd = input().split()
        if cmd[0] == '1':
            u = int(cmd[1]) - 1
            w = int(cmd[2])
            fenw.add(in_time[u], w)
            total += w
        else:
            e = int(cmd[1]) - 1
            u, v = edges[e]
            # Determine which vertex is in the subtree of the other
            if in_time[u] < in_time[v] < out_time[u]:
                sub = v
            else:
                sub = u
            sub_sum = fenw.range_sum(in_time[sub], out_time[sub])
            diff = abs(total - 2 * sub_sum)
            output.append(str(diff))

    print('\n'.join(output))

if __name__ == "__main__":
    main()