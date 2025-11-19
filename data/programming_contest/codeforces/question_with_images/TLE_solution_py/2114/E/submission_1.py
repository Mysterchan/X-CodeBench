import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    stack = [(1, 0)]
    while stack:
        node, par = stack.pop()
        parent[node] = par
        for nei in adj[node]:
            if nei != par:
                stack.append((nei, node))

    result = [0] * (n + 1)
    for u in range(1, n + 1):
        temp_sum = a[u]
        even_max = float('-inf')
        odd_max = temp_sum
        p = parent[u]
        i = 1
        while p:
            temp_sum += ((-1) ** i) * a[p]
            if i % 2 == 0:
                even_max = max(even_max, temp_sum)
            else:
                odd_max = max(odd_max, temp_sum)
            p = parent[p]
            i += 1
        result[u] = max(even_max, odd_max)

    sys.stdout.write(' '.join(str(result[i]) for i in range(1, n + 1)) + '\n')

t = int(input())
for _ in range(t):
    solve()
