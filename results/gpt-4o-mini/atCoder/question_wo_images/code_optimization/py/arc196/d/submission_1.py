import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1

    S = []
    T = []
    for _ in range(M):
        S.append(int(data[idx]) - 1); idx += 1
        T.append(int(data[idx]) - 1); idx += 1

    queries = []
    for _ in range(Q):
        l = int(data[idx]) - 1; idx += 1
        r = int(data[idx]) - 1; idx += 1
        queries.append((l, r))

    u_list = []
    v_list = []

    for i in range(M):
        u = min(S[i], T[i]) - 1
        v = max(S[i], T[i]) - 1
        u_list.append(u)
        v_list.append(v)

    results = []
    for l, r in queries:
        parent = list(range(N + 1))
        rank = [0] * (N + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        for i in range(l, r + 1):
            union(u_list[i], v_list[i])

        components = defaultdict(list)
        for i in range(N):
            components[find(i)].append(i)

        valid = True
        for i in range(l, r + 1):
            low, high = u_list[i], v_list[i] - 1
            if low <= high:
                root = find(low)
                for comp in components[root]:
                    if low <= comp <= high:
                        valid = False
                        break
            if not valid:
                break

        results.append("Yes" if valid else "No")

    print("\n".join(results))

if __name__ == "__main__":
    main()