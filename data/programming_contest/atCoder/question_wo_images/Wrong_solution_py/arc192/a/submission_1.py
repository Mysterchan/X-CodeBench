import sys
sys.setrecursionlimit(1 << 25)
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    if all((a == 0 for a in A)):
        print('No')
        return
    for i in range(N):
        if A[i] == 0 and A[(i + 1) % N] == 0:
            print('No')
            return
    parent = list(range(N))
    size = [1] * N
    edge_cnt = [0] * N

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        if size[rx] < size[ry]:
            (rx, ry) = (ry, rx)
        parent[ry] = rx
        size[rx] += size[ry]
        edge_cnt[rx] += edge_cnt[ry] + 1
    for i in range(N):
        if A[i] == 0:
            u = i
            v = (i + 2) % N
            ru = find(u)
            rv = find(v)
            if ru == rv:
                if size[ru] % 2 == 1:
                    print('No')
                    return
            else:
                if size[ru] < size[rv]:
                    (ru, rv) = (rv, ru)
                parent[rv] = ru
                size[ru] += size[rv]
                edge_cnt[ru] += edge_cnt[ru] + edge_cnt[rv] + 1
    print('Yes')
if __name__ == '__main__':
    solve()