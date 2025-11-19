import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

class SegmentTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N <<= 1
        self.tree = [0] * (2 * self.N)

    def add(self, idx, value):
        idx += self.N
        self.tree[idx] += value
        while idx > 1:
            idx >>= 1
            self.tree[idx] = self.tree[2*idx] + self.tree[2*idx + 1]

    def query(self, l, r):
        l += self.N
        r += self.N
        res = 0
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res

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

    seg = SegmentTree(n)
    for i in range(n):
        seg.add(in_time[i], 1)

    q = int(input())
    for _ in range(q):
        cmd = input().split()
        if cmd[0] == '1':
            u = int(cmd[1]) - 1
            w = int(cmd[2])
            seg.add(in_time[u], w)
        else:
            e = int(cmd[1]) - 1
            u, v = edges[e]

            if in_time[u] < in_time[v] < out_time[u]:
                sub = v
            else:
                sub = u
            sub_sum = seg.query(in_time[sub], out_time[sub])
            total = seg.query(0, n)
            print(abs(total - 2 * sub_sum))

if __name__ == "__main__":
    main()